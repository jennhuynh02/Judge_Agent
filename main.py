from judge_agent import judge_content
import json
import sys

def main():
    # Example usage
    print("Judge Agent - Content Analyzer")
    print("=" * 40)
    print("1. Analyze text")
    print("2. Analyze video")
    choice = input("Choose option (1 or 2): ").strip()
    
    if choice == "1":
        text = input("Enter text to analyze: ")
        result = judge_content(text=text)
    elif choice == "2":
        video_path = input("Enter path to video file: ").strip()
        result = judge_content(video_path=video_path)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
    
    print("\n" + "=" * 40)
    print("ANALYSIS RESULTS")
    print("=" * 40)
    print(json.dumps(result.model_dump(), indent=2))

if __name__ == "__main__":
    main()
