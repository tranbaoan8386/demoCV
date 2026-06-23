/**
 * UploadSuccess Component
 * Displays successful upload information
 * Responsibility: UI rendering only
 */

import type { UploadCVResponse } from '../types/uploadCV.types';

interface UploadSuccessProps {
  result: UploadCVResponse;
  onReset: () => void;
}

export const UploadSuccess = ({
  result,
  onReset,
}: UploadSuccessProps) => {
  const createdDate = new Date(result.created_at).toLocaleString();

  return (
    <div className="p-4 bg-green-50 border border-green-200 rounded-md">
      <h3 className="text-lg font-semibold text-green-800 mb-3">
        ✓ Upload Successful
      </h3>
      <div className="space-y-2 text-sm text-green-700 mb-4">
        <p>
          <span className="font-semibold">Filename:</span>{' '}
          {result.original_filename}
        </p>
        <p>
          <span className="font-semibold">Status:</span> {result.status}
        </p>
        <p>
          <span className="font-semibold">Uploaded:</span> {createdDate}
        </p>
      </div>
      <button
        onClick={onReset}
        className="w-full px-4 py-2 bg-green-600 text-white font-semibold rounded-md hover:bg-green-700 transition-colors duration-200"
      >
        Upload Another CV
      </button>
    </div>
  );
};
