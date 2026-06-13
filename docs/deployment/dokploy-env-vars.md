# SPX Voice — Dokploy Deployment Environment Variables

## Domains

| Service | Domain | Port |
|---|---|---|
| UI (main app) | `dogra.cis.bz` | 3010 |
| API | `api.dogra.cis.bz` | 8000 |

---

## Required Environment Variables

Set these in the Dokploy dashboard under your stack's environment variables.

| Variable | Value | Notes |
|---|---|---|
| `POSTGRES_PASSWORD` | `15cffdcafc6644edb600260624e1d9ae` | Postgres superuser password |
| `REDIS_PASSWORD` | `4faf4be59d214d2da78982350b59a506` | Redis AUTH password |
| `MINIO_ROOT_PASSWORD` | `96264f61c4794f0684cea4f3f6785f6d` | MinIO admin password |
| `OSS_JWT_SECRET` | `c30ca5b031804ebc846ea98085114973` | JWT signing secret for local auth |
| `APP_URL` | `https://dogra.cis.bz` | Browser-facing UI root URL |
| `BACKEND_API_ENDPOINT` | `https://api.dogra.cis.bz` | Browser-facing API URL |
| `UI_APP_URL` | `https://dogra.cis.bz` | Browser-facing UI URL |
| `MINIO_PUBLIC_ENDPOINT` | `https://dogra.cis.bz` | Browser-facing MinIO URL (proxied through Next.js) |

---

## AI Provider Keys

At least one of the Google/Gemini keys is required for voice agents to work.

| Variable | Value | Notes |
|---|---|---|
| `GOOGLE_API_KEY` | `your-key-here` | Google AI / Gemini API key |
| `GEMINI_API_KEY` | `your-key-here` | Alternative Gemini key var |
| `OPENAI_API_KEY` | `your-key-here` | Only if using OpenAI models |
| `DEEPGRAM_API_KEY` | `your-key-here` | Only if using Deepgram STT |
| `ELEVENLABS_API_KEY` | `your-key-here` | Only if using ElevenLabs TTS |

---

## LiveKit (required for voice)

| Variable | Value | Notes |
|---|---|---|
| `LIVEKIT_URL` | `wss://livekit.your-server.com` | LiveKit server WebSocket URL |
| `LIVEKIT_API_KEY` | `your-livekit-api-key` | LiveKit API key |
| `LIVEKIT_API_SECRET` | `your-livekit-api-secret` | LiveKit API secret |

---

## Optional Variables

| Variable | Default | Notes |
|---|---|---|
| `POSTGRES_USER` | `postgres` | Postgres user |
| `POSTGRES_DB` | `spx_voice` | Postgres database name |
| `MINIO_ROOT_USER` | `minioadmin` | MinIO admin username |
| `MINIO_BUCKET` | `voice-audio` | MinIO bucket name |
| `ALLOW_PUBLIC_SIGNUP` | `false` | Allow self-registration |
| `SINGLE_ORGANIZATION_MODE` | `true` | Single-tenant mode |
| `LOG_LEVEL` | `INFO` | Python log level |
| `FASTAPI_WORKERS` | `1` | Number of uvicorn workers |
| `ARQ_WORKERS` | `1` | Number of ARQ background workers |
| `ENABLE_TELEMETRY` | `false` | PostHog telemetry |
| `LANGFUSE_HOST` | *(none)* | Langfuse self-hosted URL |
| `LANGFUSE_PUBLIC_KEY` | *(none)* | Langfuse public key |
| `LANGFUSE_SECRET_KEY` | *(none)* | Langfuse secret key |
| `POSTHOG_API_KEY` | *(none)* | PostHog API key |
| `POSTHOG_HOST` | *(none)* | PostHog host |
| `VOICE_RUNTIME` | `livekit` | Voice runtime engine |
| `DEFAULT_REALTIME_MODEL` | `gemini-3.1-flash-live-preview` | Default Gemini realtime model |
| `LIVEKIT_AGENT_NAME` | `spx-voice` | LiveKit agent name |
| `LIVEKIT_ROOM_PREFIX` | `spx-voice` | LiveKit room prefix |
| `LIVEKIT_WORKER_MANAGED_BY_API` | `true` | Let API manage LiveKit worker |
