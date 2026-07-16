// Prototype mock data (used by Billing/Admin pages and mock API mode).
export const plans = [
  { code: 'free', name: 'Free', price: '0 €', highlighted: false, features: ['1 nivel', 'Tarjetas limitadas', '5 solicitudes IA/día'] },
  { code: 'pro', name: 'Pro', price: '14,99 €', highlighted: true, features: ['Tutor de voz IA', 'Subida de audio/PDF', 'Podcast e imágenes'] },
  { code: 'premium', name: 'Premium', price: '24,99 €', highlighted: false, features: ['Vídeo y transcripción', 'DELE/SIELE', 'Plan personal'] }
];
