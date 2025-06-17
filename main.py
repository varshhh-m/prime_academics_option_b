#!/usr/bin/env python3

import os
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv('OPENAI_API_KEY')
print(f" DEBUG INFO:")
print(f"   API Key found: {bool(api_key)}")
print(f"   API Key length: {len(api_key) if api_key else 0}")
print(f"   Starts with sk-proj: {api_key.startswith('sk-proj') if api_key else False}")
print()


try:
    import openai
    print(" OpenAI package imported successfully")
    print(f"   OpenAI version: {openai.__version__}")
except ImportError as e:
    print(f" OpenAI import failed: {e}")
except Exception as e:
    print(f" OpenAI import issue: {e}")
print()

from summary_generator import EducationalSummaryGenerator

def main():
    
    
    print(" PRIME ACADEMICS INTERNSHIP APPLICATION")
    print("OPTION B: Prompt Engineering + Summary Generation")
    print("=" * 60)
    print()
    
   
    transcript_file = None
    possible_files = [
        'tutoring_transcript.txt',
        'Tutoring_Transcript_File.txt',
        'transcript.txt'
    ]
    
    for filename in possible_files:
        if os.path.exists(filename):
            transcript_file = filename
            print(f" Found transcript: {filename}")
            break
    
    if not transcript_file:
        print(" No transcript file found - using sample data")
        print(" To use your own transcript, save it as 'tutoring_transcript.txt'")
    
    print()
    
    
    try:
        generator = EducationalSummaryGenerator()
        result = generator.generate_summary(transcript_file)
        
        if result:
            print("\n OPTION B SUBMISSION READY!")
            print("\n GENERATED PARENT SUMMARY:")
            print("-" * 50)
            print(result['parent_summary'][:500] + "...")
            print("\n[Full summary saved to file]")
            
            print("\n PROMPT DESIGN EXPLANATION:")
            print("-" * 50)
            print(result['prompt_design_explanation'][:300] + "...")
            print("\n[Full explanation saved to file]")
            
            print("\n FILES FOR PRIME ACADEMICS APPLICATION:")
            print("   1. parent_email_summary_[timestamp].txt - ATTACH THIS")
            print("   2. prompt_engineering_explanation_[timestamp].txt - ATTACH THIS")
            
            print("\n OPTION B COMPLETE! Ready for submission! 🎓")
        else:
            print("Generation failed")
            
    except Exception as e:
        print(f" Error: {e}")
        print(" Make sure you have the required packages installed:")
        print("   pip install openai python-dotenv")

if __name__ == "__main__":
    main()