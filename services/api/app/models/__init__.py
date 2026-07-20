from app.models.user import User, UserProfile
from app.models.subscription import Plan, Subscription, BillingCustomer, Invoice, PaymentEvent, UserEntitlement, UsageCounter
from app.models.course import CEFRLevel, CourseModule, Lesson, LessonProgress, LessonTranslation
from app.models.upload import UploadedFile, ExtractedText, Transcript, TextAnalysis
from app.models.flashcard import FlashcardDeck, Flashcard, FlashcardReview
from app.models.exercise import Exercise, ExerciseSubmission
from app.models.vocabulary import VocabularyItem, UserVocabulary, UserMistake
from app.models.voice import VoiceSession, VoiceMessage
from app.models.podcast import Podcast, PodcastSegment
from app.models.generated import GeneratedImage, GeneratedAudio
from app.models.usage import AIUsageLog, AuditLog, AdminAuditLog, BackgroundJob, SystemEvent, FeatureFlag
from app.models.license import License, LicenseActivation
from app.models.diagnostic import DiagnosticResult
from app.models.motivation import MotivationState
