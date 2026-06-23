/**
 * useUploadCV Hook
 * Manages upload state and orchestrates the upload flow
 * Responsibilities: state management + orchestration only (no API calls)
 */

import { useState } from 'react';
import { uploadCVService } from '../services/uploadCVService';
import type { UploadCVResponse } from '../types/uploadCV.types';

interface UploadState {
  file: File | null;
  loading: boolean;
  result: UploadCVResponse | null;
  error: string | null;
}

export const useUploadCV = () => {
  const [state, setState] = useState<UploadState>({
    file: null,
    loading: false,
    result: null,
    error: null,
  });

  const selectFile = (file: File | null) => {
    setState((prev) => ({
      ...prev,
      file,
      error: null, // Clear error when new file is selected
    }));
  };

  const upload = async () => {
    if (!state.file) {
      setState((prev) => ({ ...prev, error: 'No file selected' }));
      return;
    }

    setState((prev) => ({ ...prev, loading: true, error: null }));

    try {
      const result = await uploadCVService.upload(state.file);
      setState((prev) => ({ ...prev, result, loading: false }));
    } catch (err) {
      const errorMessage =
        err instanceof Error ? err.message : 'Upload failed';
      setState((prev) => ({ ...prev, error: errorMessage, loading: false }));
    }
  };

  const reset = () => {
    setState({
      file: null,
      loading: false,
      result: null,
      error: null,
    });
  };

  return {
    file: state.file,
    loading: state.loading,
    result: state.result,
    error: state.error,
    selectFile,
    upload,
    reset,
  };
};
