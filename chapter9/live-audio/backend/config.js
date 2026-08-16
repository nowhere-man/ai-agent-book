const config = {
  // API Keys
  OPENAI_API_KEY: process.env.OPENAI_API_KEY || 'your-openai-api-key-here',
  ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY || 'your-anthropic-api-key-here',
  FISH_API_KEY: process.env.FISH_API_KEY || 'your-fish-api-key-here',

  // Provider Selection
  ASR_PROVIDER: 'openai',
  LLM_PROVIDER: 'openai',
  TTS_PROVIDER: 'openai',

  // ASR Configuration
  ASR_PROVIDERS: {
    openai: {
      apiUrl: 'https://api.openai.com/v1/audio/transcriptions',
      model: 'whisper-1',
      apiKey: 'OPENAI_API_KEY'
    }
  },

  // LLM Configuration
  LLM_PROVIDERS: {
    openai: {
      apiUrl: 'https://api.openai.com/v1/chat/completions',
      model: 'gpt-4o',
      apiKey: 'OPENAI_API_KEY'
    }
  },

  // TTS Configuration
  TTS_PROVIDERS: {
    openai: {
      apiUrl: 'https://api.openai.com/v1/audio/speech',
      model: 'tts-1',
      voice: 'alloy',
      apiKey: 'OPENAI_API_KEY'
    },
    fish: {
      model: 's1',
      apiKey: 'FISH_API_KEY'
    }
  },

  // Legacy support (will be deprecated)
  LLM_MODEL: 'gpt-4o',
  LLM_API_URL: 'https://api.openai.com/v1/chat/completions',
  STT_API_URL: 'https://api.openai.com/v1/audio/transcriptions',
  STT_MODEL: 'whisper-1',
  TTS_API_URL: 'https://api.openai.com/v1/audio/speech',

  // Common Configuration
  VISION_MAX_TOKENS: 4096,

  // Silero VAD Configuration
  VAD_THRESHOLD: 0.5,                  // Speech probability threshold for Silero VAD (0.0 to 1.0)
  VAD_FRAME_LENGTH: 512,               // Frame length for VAD analysis (samples)
  VAD_MIN_SPEECH_DURATION: 250,        // Minimum speech duration in ms
  VAD_MAX_SILENCE_DURATION: 500,       // Maximum silence duration before ending speech in ms
  AUDIO_SAMPLE_RATE: 16000,            // Sample rate for audio processing (required for Silero VAD)
  AUDIO_CHUNK_SIZE: 4096,              // Audio chunk size for processing

  // Server Configuration
  LISTEN_PORT: 8848,
  LISTEN_HOST: '0.0.0.0',
  SYSTEM_PROMPT: 'You are a helpful AI assistant.',
  CANCEL_PLAYBACK_TIME_THRESHOLD: 3000,
};

module.exports = config;
