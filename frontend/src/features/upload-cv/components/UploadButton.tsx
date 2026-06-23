/**
 * UploadButton Component
 * Renders upload button with loading state
 * Responsibility: UI rendering only
 */

interface UploadButtonProps {
  onClick: () => void;
  disabled: boolean;
  loading: boolean;
}

export const UploadButton = ({
  onClick,
  disabled,
  loading,
}: UploadButtonProps) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled || loading}
      className="w-full px-4 py-2 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors duration-200 flex items-center justify-center gap-2"
    >
      {loading && (
        <svg
          className="animate-spin h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            className="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            strokeWidth="4"
          />
          <path
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          />
        </svg>
      )}
      {loading ? 'Uploading...' : 'Upload CV'}
    </button>
  );
};
