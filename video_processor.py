import subprocess
import base64
import os
from typing import Dict, List

def extract_keyframes(video_path: str, max_frames: int = 8) -> List[str]:
    """Extract keyframes from video and encode as base64"""
    # TODO: Implement ffmpeg frame extraction
    # Expected: Extract 1 frame every 10 seconds, max 8 frames
    # Command: ffmpeg -i video_path -vf "select='not(mod(n\,300))'" -vsync 0 -frames:v 8 output_%03d.jpg
    # Return: List of base64-encoded frame strings
    pass

def transcribe_audio(video_path: str) -> str:
    """Extract and transcribe audio from video using OpenAI Whisper"""
    # TODO: Implement audio extraction and Whisper API call
    # Step 1: Extract audio with ffmpeg: ffmpeg -i video_path -vn -acodec pcm_s16le audio.wav
    # Step 2: Call OpenAI Whisper API with audio file
    # Return: Transcribed text
    pass

def process_video(video_path: str) -> Dict[str, any]:
    """Process video file and return transcript + keyframes"""
    # TODO: Orchestrate video processing
    # Expected: Call extract_keyframes() and transcribe_audio()
    # Return: {"transcript": str, "keyframes": List[str]}
    
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    # Placeholder return structure
    return {
        "transcript": "",  # TODO: Get from transcribe_audio()
        "keyframes": []    # TODO: Get from extract_keyframes()
    }
