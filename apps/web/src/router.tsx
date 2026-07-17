import { createBrowserRouter, Navigate, Outlet } from 'react-router-dom';
import { AppShell } from './components/layout/AppShell';
import { useAuth } from './store/auth';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import CoursePage from './pages/CoursePage';
import TextAnalyzerPage from './pages/TextAnalyzerPage';
import UploadStudioPage from './pages/UploadStudioPage';
import PodcastStudioPage from './pages/PodcastStudioPage';
import VoiceTutorPage from './pages/VoiceTutorPage';
import SimulationsPage from './pages/SimulationsPage';
import SettingsPage from './pages/SettingsPage';
import DiagnosticPage from './pages/DiagnosticPage';
import ProgressPage from './pages/ProgressPage';
import ReviewPage from './pages/ReviewPage';
import FlashcardsPage from './pages/FlashcardsPage';
import BillingPage from './pages/BillingPage';
import AdminPage from './pages/AdminPage';

function Protected() {
  const token = useAuth((s) => s.token);
  if (!token) return <Navigate to="/login" replace />;
  return <AppShell><Outlet /></AppShell>;
}

export const router = createBrowserRouter([
  { path: '/', element: <LandingPage /> },
  { path: '/login', element: <LoginPage /> },
  {
    path: '/app',
    element: <Protected />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: 'diagnostic', element: <DiagnosticPage /> },
      { path: 'course', element: <CoursePage /> },
      { path: 'upload', element: <UploadStudioPage /> },
      { path: 'podcasts', element: <PodcastStudioPage /> },
      { path: 'analyzer', element: <TextAnalyzerPage /> },
      { path: 'voice', element: <VoiceTutorPage /> },
      { path: 'simulations', element: <SimulationsPage /> },
      { path: 'settings', element: <SettingsPage /> },
      { path: 'flashcards', element: <FlashcardsPage /> },
      { path: 'review', element: <ReviewPage /> },
      { path: 'progress', element: <ProgressPage /> },
      { path: 'billing', element: <BillingPage /> },
      { path: 'admin', element: <AdminPage /> }
    ]
  },
  { path: '*', element: <Navigate to="/" replace /> }
]);
