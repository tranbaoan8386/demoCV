/**
 * Type definitions for Upload CV feature
 * Defines the response structure from the backend API
 */

export interface UploadCVResponse {
  id: string;
  original_filename: string;
  object_name: string;
  status: string;
  created_at: string;
}
