"""
Mock API responses for testing without real API keys.
Set USE_MOCK = True in config.py to use these instead of real API calls.
"""

from typing import Dict, Any, List
from models import ViralityScore

def mock_gptzero_response(text: str) -> Dict[str, Any]:
    """Mock GPTZero API response"""
    # Simulate AI detection based on simple heuristics
    ai_indicators = ["furthermore", "moreover", "in conclusion", "it is important to note"]
    ai_score = sum(1 for indicator in ai_indicators if indicator.lower() in text.lower())
    
    if ai_score >= 2:
        classification = "ai"
        confidence = 0.85
    elif ai_score == 1:
        classification = "ai-assisted"
        confidence = 0.65
    else:
        classification = "human"
        confidence = 0.75
    
    return {
        "documents": [{
            "classification": classification,
            "confidence": confidence,
            "completely_generated_prob": confidence if classification == "ai" else 1 - confidence
        }]
    }

def mock_gpt4o_virality(text: str) -> ViralityScore:
    """Mock GPT-4o virality scoring"""
    # Simple heuristics for demo purposes
    text_lower = text.lower()
    
    # Emotional trigger: check for emotional words
    emotional_words = ["amazing", "shocking", "incredible", "wow", "omg", "love", "hate"]
    emotional_trigger = min(25, len([w for w in emotional_words if w in text_lower]) * 5 + 10)
    
    # Hook quality: check if starts with question or strong statement
    hook_quality = 20 if text.startswith(("?", "!", "How", "Why", "What")) else 12
    
    # Novelty: random but reasonable
    novelty = 15
    
    # Compression: shorter texts score higher
    compression = min(25, max(5, 25 - len(text) // 50))
    
    total = emotional_trigger + hook_quality + novelty + compression
    
    return ViralityScore(
        emotional_trigger=emotional_trigger,
        hook_quality=hook_quality,
        novelty=novelty,
        compression=compression,
        total=total
    )

def mock_gpt4o_distribution(text: str) -> List[str]:
    """Mock GPT-4o distribution analysis"""
    text_lower = text.lower()
    
    # Simple keyword-based distribution
    distributions = []
    
    if any(word in text_lower for word in ["tech", "ai", "code", "software", "startup"]):
        distributions.append("Tech Twitter")
    if any(word in text_lower for word in ["professional", "career", "business", "leadership"]):
        distributions.append("LinkedIn")
    if any(word in text_lower for word in ["meme", "funny", "lol", "reddit"]):
        distributions.append("Reddit")
    if any(word in text_lower for word in ["video", "viral", "trend", "dance"]):
        distributions.append("TikTok")
    
    # Default if no matches
    if not distributions:
        distributions = ["Mainstream News", "YouTube"]
    
    return distributions[:3]  # Max 3

def mock_gpt4o_explanation(text: str, origin: str, virality: ViralityScore, distribution: List[str]) -> str:
    """Mock GPT-4o explanation generation"""
    return f"""This content was classified as {origin}-generated with moderate confidence. 
The virality score of {virality.total}/100 reflects {_describe_virality(virality)}. 
The content is most likely to resonate with {', '.join(distribution)} audiences based on its 
topic, tone, and style. This analysis is based on content-intrinsic signals without external 
data sources."""

def _describe_virality(virality: ViralityScore) -> str:
    """Helper to describe virality components"""
    components = []
    if virality.emotional_trigger > 15:
        components.append("strong emotional appeal")
    if virality.hook_quality > 15:
        components.append("effective hook")
    if virality.novelty > 15:
        components.append("novel content")
    if virality.compression > 15:
        components.append("concise messaging")
    
    return ", ".join(components) if components else "moderate viral potential"
