/**
 * UploadCVPage
 * Page component that composes the upload CV feature
 * Responsibility: Page composition and layout only
 */

import { useUploadCV } from '../hooks/useUploadCV';
import { FileInput } from '../components/FileInput';
import { UploadButton } from '../components/UploadButton';
import { UploadSuccess } from '../components/UploadSuccess';
import { UploadError } from '../components/UploadError';

export const UploadCVPage = () => {
  const { file, loading, result, error, selectFile, upload, reset } =
    useUploadCV();

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4 flex items-center justify-center">
      <div className="w-full max-w-md bg-white rounded-lg shadow-lg p-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">Upload CV</h1>
        <p className="text-gray-600 mb-6">
          Upload your PDF resume to get started
        </p>

        {result ? (
          <UploadSuccess result={result} onReset={reset} />
        ) : error ? (
          <>
            <UploadError error={error} onReset={reset} />
            <div className="mt-4">
              <FileInput
                file={file}
                onChange={selectFile}
                disabled={loading}
              />
            </div>
          </>
        ) : (
          <>
            <FileInput file={file} onChange={selectFile} disabled={loading} />
            <div className="mt-4">
              <UploadButton
                onClick={upload}
                disabled={!file}
                loading={loading}
              />
            </div>
          </>
        )}
      </div>
    </div>
  );
};
