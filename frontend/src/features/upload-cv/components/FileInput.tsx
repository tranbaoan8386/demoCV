/**
 * FileInput Component
 * Renders controlled file input for CV selection
 * Responsibility: UI rendering only
 */

interface FileInputProps {
  file: File | null;
  onChange: (file: File | null) => void;
  disabled: boolean;
}

export const FileInput = ({ file, onChange, disabled }: FileInputProps) => {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0] || null;
    onChange(selectedFile);
  };

  return (
    <div className="space-y-2">
      <label className="block text-sm font-medium text-gray-700">
        Select PDF File
      </label>
      <input
        type="file"
        accept=".pdf"
        onChange={handleChange}
        disabled={disabled}
        className="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed"
      />
      {file && (
        <p className="text-sm text-gray-600">
          Selected: <span className="font-semibold">{file.name}</span>
        </p>
      )}
    </div>
  );
};
