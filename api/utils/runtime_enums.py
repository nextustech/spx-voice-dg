from enum import Enum


class RealtimeFeedbackType(str, Enum):
    USER_TRANSCRIPTION = "user_transcription"
    BOT_TEXT = "bot_text"
    FUNCTION_CALL_START = "function_call_start"
    FUNCTION_CALL_END = "function_call_end"
    LATENCY_MEASURED = "latency_measured"
    TTFB_METRIC = "ttfb_metric"
    PIPELINE_ERROR = "pipeline_error"
    NODE_TRANSITION = "node_transition"
    BOT_STARTED_SPEAKING = "bot_started_speaking"
    BOT_STOPPED_SPEAKING = "bot_stopped_speaking"
    USER_MUTE_STARTED = "user_mute_started"
    USER_MUTE_STOPPED = "user_mute_stopped"


class EndTaskReason(str, Enum):
    USER_HANGUP = "user_hangup"
    USER_QUALIFIED = "user_qualified"
    END_CALL_TOOL_REASON = "end_call_tool"
    UNEXPECTED_ERROR = "unexpected_error"
    TRANSFER_CALL = "transfer_call"
    USER_IDLE_MAX_DURATION_EXCEEDED = "user_idle_max_duration_exceeded"
    CALL_DURATION_EXCEEDED = "call_duration_exceeded"
    PIPELINE_ERROR = "pipeline_error"
    VOICEMAIL_DETECTED = "voicemail_detected"
