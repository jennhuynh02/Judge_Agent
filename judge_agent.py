import requests
import json
from typing import Dict, Any, List, Optional
from models import JudgeResult, ViralityScore
from video_processor import process_video
import config

# Import mock functions if in mock mode
if config.USE_MOCK:
    from mock_api import (
        mock_gptzero_response,
        mock_gpt4o_virality,
        mock_gpt4o_distribution,
        mock_gpt4o_explanation
    )

def call_gptzero(text: str) -> Dict[str, Any]:
    """Call GPTZero API for origin detection"""
    if config.USE_MOCK:
        return mock_gptzero_response(text)
    
    # TODO: Implement HTTP POST to GPTZero
    # Expected: POST to config.GPTZERO_ENDPOINT with headers and JSON payload
    # Return: GPTZero response with classification and confidence
    headers = {
        "X-Api-Key": config.GPTZERO_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"document": text}
    # response = requests.post(config.GPTZERO_ENDPOINT, headers=headers, json=payload)
    # return response.json()
    pass

def call_gpt4o_virality(text: str) -> ViralityScore:
    """Call GPT-4o for virality scoring"""
    if config.USE_MOCK:
        return mock_gpt4o_virality(text)
    
    # TODO: Implement structured output call
    # Expected: POST to OpenAI API with response_format for JSON
    # Return: ViralityScore with all four sub-signals
    pass

def call_gpt4o_distribution(text: str) -> List[str]:
    """Call GPT-4o for distribution analysis"""
    if config.USE_MOCK:
        return mock_gpt4o_distribution(text)
    
    # TODO: Implement distribution mapping
    # Expected: POST to OpenAI API with taxonomy prompt
    # Return: List of 1-3 audience targets
    pass

def call_gpt4o_explanation(text: str, origin: str, virality: ViralityScore, distribution: List[str]) -> str:
    """Call GPT-4o to generate explanation"""
    if config.USE_MOCK:
        return mock_gpt4o_explanation(text, origin, virality, distribution)
    
    # TODO: Aggregate results and generate explanation
    # Expected: POST to OpenAI API with all upstream results
    # Return: Concise explanation string
    pass

def judge_content(text: Optional[str] = None, video_path: Optional[str] = None) -> JudgeResult:
    """Main function to judge content (text or video)"""
    
    # Process video if provided
    content_text = text
    video_data = None
    
    if video_path:
        # TODO: Process video file
        video_data = process_video(video_path)
        # Combine transcript with any provided text
        content_text = video_data.get("transcript", "")
        if text:
            content_text = f"{text}\n\nTranscript: {content_text}"
    
    if not content_text:
        raise ValueError("Must provide either text or video_path")
    
    # Step 1: Origin detection
    gptzero_result = call_gptzero(content_text)
    
    if config.USE_MOCK:
        # Parse mock response
        origin = gptzero_result["documents"][0]["classification"]
        origin_confidence = gptzero_result["documents"][0]["confidence"]
    else:
        # TODO: Parse real GPTZero response
        origin = "human"
        origin_confidence = 0.0
    
    # Step 2: Virality scoring
    # TODO: Pass video_data["keyframes"] to GPT-4o vision if available
    virality = call_gpt4o_virality(content_text)
    
    # Step 3: Distribution mapping
    distribution = call_gpt4o_distribution(content_text)
    
    # Step 4: Generate explanation
    explanation = call_gpt4o_explanation(content_text, origin, virality, distribution)
    
    return JudgeResult(
        origin=origin,
        origin_confidence=origin_confidence,
        virality=virality,
        distribution=distribution,
        explanation=explanation
    )
