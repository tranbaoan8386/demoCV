/**
 * UploadError Component
 * Displays upload error message
 * Responsibility: UI rendering only
 */

interface UploadErrorProps {
  error: string;
  onReset: () => void;
}

export const UploadError = ({ error, onReset }: UploadErrorProps) => {
  return (
    <div className="p-4 bg-red-50 border border-red-200 rounded-md">
      <h3 className="text-lg font-semibold text-red-800 mb-2">
        ✕ Upload Failed
      </h3>
      <p className="text-sm text-red-700 mb-4">{error}</p>
      <button
        onClick={onReset}
        className="w-full px-4 py-2 bg-red-600 text-white font-semibold rounded-md hover:bg-red-700 transition-colors duration-200"
      >
        Try Again
      </button>
    </div>
  );
};
