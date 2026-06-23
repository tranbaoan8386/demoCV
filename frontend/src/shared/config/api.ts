/**
 * Centralized API configuration
 * Reads base URL from environment variables to avoid hardcoding
 */

export const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000";
