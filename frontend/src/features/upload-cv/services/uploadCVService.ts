/**
 * Upload CV Service
 * Handles API communication for CV uploads
 * Single responsibility: HTTP POST requests only
 */

import { API_BASE_URL } from '@/shared/config/api';
import type { UploadCVResponse } from '../types/uploadCV.types';

export const uploadCVService = {
  async upload(file: File): Promise<UploadCVResponse> {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(`${API_BASE_URL}/cvs/upload`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(
        error.detail || `Upload failed with status ${response.status}`
      );
    }

    return response.json();
  },
};
