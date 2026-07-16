// Frontend runtime config.
// - Dev (no docker): VITE_API_URL=http://localhost:8000
// - Docker/self-hosted: VITE_API_URL="" so requests hit same-origin /api via nginx.
const raw = import.meta.env.VITE_API_URL as string | undefined;
export const config = {
  apiUrl: raw === undefined ? 'http://localhost:8000' : raw,
  useMock: (import.meta.env.VITE_USE_MOCK ?? 'false') === 'true'
};
