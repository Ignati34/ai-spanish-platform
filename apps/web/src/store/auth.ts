import { create } from 'zustand';
import { api } from '../lib/api';

interface AuthState {
  token: string | null;
  setToken: (t: string | null) => void;
  logout: () => void;
}

export const useAuth = create<AuthState>((set) => ({
  token: localStorage.getItem('access_token'),
  setToken: (t) => { api.setToken(t); set({ token: t }); },
  logout: () => { api.setToken(null); set({ token: null }); }
}));
