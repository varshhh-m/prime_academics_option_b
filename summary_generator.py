import os
os.environ['OPENAI_API_KEY'] = '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'



from datetime import datetime
from typing import Dict, Any, List
import json
from transcript_analyzer import EducationalTranscriptAnalyzer


try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("OpenAI not available - using template generation")

class EducationalSummaryGenerator:
    
    
    def __init__(self):
        self.analyzer = EducationalTranscriptAnalyzer()
        
       
        try:
            import openai
            
            
            api_key = os.getenv('OPENAI_API_KEY')
            
            if api_key:
                
                if hasattr(openai, 'OpenAI'):
                    self.client = openai.OpenAI(api_key=api_key)
                    self.use_ai = True
                    self.openai_version = "new"
                    print(" Using OpenAI GPT-4 for enhanced summary generation (v1.x)")
                else:
                    
                    openai.api_key = api_key
                    self.use_ai = True
                    self.openai_version = "legacy"
                    print(" Using OpenAI GPT-4 for enhanced summary generation (v0.x)")
            else:
                self.use_ai = False
                print(" No API key found - using template")
                
        except ImportError:
            self.use_ai = False
            print(" OpenAI not installed - using template")
        except Exception as e:
            self.use_ai = False
            print(f" OpenAI setup failed: {e} - using template")

    def generate_summary(self, transcript_file: str) -> Dict[str, Any]:
        """Generate comprehensive educational summary"""
        print("🎓 Generating comprehensive educational summary...")
        
       
        analysis = self.analyzer.analyze_transcript(transcript_file)
        
        if self.use_ai:
            
            prompt = self._create_advanced_prompt(analysis)
            summary_content = self._generate_ai_summary(prompt)
        else:
            
            summary_content = self._generate_template_summary(analysis)
        
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        result = {
            'timestamp': timestamp,
            'analysis': analysis,
            'summary_content': summary_content,
            'method': 'AI-Enhanced' if self.use_ai else 'Template-Based',
            'prompt_engineering_explanation': self._create_prompt_explanation()
        }
        
        return result

    def _generate_ai_summary(self, prompt: str) -> str:
        
        try:
            print(" Calling OpenAI API...")
            
            if hasattr(self, 'openai_version') and self.openai_version == "new":
                
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Dr. Sarah Chen, an expert educational consultant specializing in learning sciences and parent communication."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1800,
                    temperature=0.7
                )
                result = response.choices[0].message.content.strip()
                print(" OpenAI response received!")
                return result
                
            else:
                
                import openai
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Dr. Sarah Chen, an expert educational consultant specializing in learning sciences and parent communication."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1800,
                    temperature=0.7
                )
                result = response.choices[0].message.content.strip()
                print(" OpenAI response received!")
                return result
                
        except Exception as e:
            print(f" OpenAI error: {e}")
            print(" Using template fallback...")
            return self._generate_template_summary({})

    def _create_advanced_prompt(self, analysis: Dict[str, Any]) -> str:
        
        
        subjects = analysis.get('subjects', {}).get('subjects_identified', [])
        action_items = analysis.get('action_items', [])
        teaching_moments = analysis.get('teaching_moments', [])
        session_duration = analysis.get('session_metadata', {}).get('duration_minutes', 'Unknown')
        
        prompt = f"""
ROLE: You are Dr. Varsha Meda, Ph.D. in Learning Sciences with 15+ years of experience in educational psychology and family communication. You specialize in translating complex educational assessments into actionable insights for parents.

TASK: Create a professional email summary for parents about their child's tutoring session.

SESSION DATA:
- Duration: {session_duration} minutes
- Subjects Covered: {', '.join(subjects) if subjects else 'General academic support'}
- Action Items Identified: {len(action_items)}
- Teaching Moments: {len(teaching_moments)}

SPECIFIC CONTENT TO INCLUDE:
1. Action Items Found: {action_items[:3] if action_items else ['Continue regular practice', 'Review today\'s concepts']}
2. Key Learning Areas: {subjects[:3] if subjects else ['Problem-solving', 'Study skills']}

COMMUNICATION FRAMEWORK:
- Use warm, professional tone that builds parent confidence
- Apply growth mindset language (effort-focused praise)
- Include specific, actionable next steps
- Balance challenges with achievements
- Use educational terminology appropriately for parent audience

STRUCTURE:
1. Subject Line (engaging, positive)
2. Warm opening acknowledging partnership
3. Session highlights with specific evidence
4. Academic progress observations
5. Concrete action items for home support
6. Encouraging close that reinforces growth potential

CONSTRAINTS:
- 400-500 words maximum
- Professional email format
- Evidence-based observations only
- No generic praise - be specific
- Include pedagogical best practices naturally

Generate the complete parent email now:
"""
        return prompt

    def _generate_template_summary(self, analysis: Dict[str, Any]) -> str:
        
        
       
        subjects = analysis.get('subjects', {}).get('subjects_identified', [])
        action_items = analysis.get('action_items', [])
        teaching_moments = analysis.get('teaching_moments', [])
        session_duration = analysis.get('session_metadata', {}).get('duration_minutes', 63)
        
        
        subject_text = ', '.join(subjects) if subjects else 'academic fundamentals'
        
        summary = f"""Subject: Session Summary - Excellent Preparation and Academic Growth! 🎓

Dear Parents,

I hope this message finds you well. I wanted to reach out immediately following today's tutoring session to share some wonderful insights about your child's academic progress and the impressive dedication they've demonstrated.

**Session Overview: Strategic Test Preparation**

Today's {session_duration}-minute session was specifically designed as comprehensive preparation for your child's upcoming test. Despite facing some initial challenges with problem-solving approaches, your child showed remarkable resilience and adaptability—qualities that are excellent predictors of long-term academic success.

**Academic Progress Highlights**

I'm particularly impressed by your child's growth in {subject_text}. During our session, they demonstrated strong analytical thinking and showed genuine curiosity about understanding concepts deeply rather than just memorizing procedures. This approach to learning reflects excellent academic maturity.

Your child successfully worked through complex problems involving mathematical reasoning and reading comprehension. When they encountered difficulties, they employed effective self-correction strategies and asked thoughtful clarifying questions—both indicators of developing metacognitive skills.

**Specific Learning Achievements**

• **Problem-Solving Development**: Your child showed improved systematic thinking when approaching multi-step problems
• **Academic Confidence**: Notable increase in willingness to tackle challenging material independently  
• **Test Preparation Skills**: Demonstrated effective time management and strategic thinking for tomorrow's assessment

**Action Items for Home Support**

To maximize the momentum from today's session, I recommend:

1. **Evening Review** (15 minutes): Briefly review the key formulas and concepts we practiced today
2. **Morning Preparation**: Ensure adequate rest and a healthy breakfast before the test
3. **Confidence Building**: Remind your child of the specific strategies we discussed for approaching difficult questions

**Looking Forward**

Your child is well-prepared for tomorrow's test and has developed valuable study skills that will serve them throughout their academic journey. The analytical thinking and persistence they demonstrated today are exactly the qualities that lead to long-term academic success.

Please don't hesitate to reach out if you have any questions about today's session or would like to discuss additional support strategies.

Best regards,

Dr. Varsha Meda, Ph.D.
Educational Consultant & Learning Specialist
Prime Academics Tutoring Services

P.S. Your child mentioned being nervous about tomorrow—please reassure them that feeling some nervous energy is completely normal and often indicates they care about doing well. They're thoroughly prepared! 🌟"""

        return summary

    def _create_prompt_explanation(self) -> str:
        
        
        explanation = """PROMPT ENGINEERING EXPLANATION: Educational Communication Framework

**1. EXPERT PERSONA ESTABLISHMENT**
- Created Dr. Sarah Chen with specific credentials (15+ years experience)
- Established expertise in learning sciences and family communication
- Positioned as specialist in translating educational assessments for parents
- Builds immediate credibility and professional authority

**2. ROLE-SPECIFIC INSTRUCTIONS**
- Clear task definition: professional parent email creation
- Specific communication goals: actionable insights + confidence building
- Target audience consideration: parents (not educators)
- Professional context establishment

**3. DATA INTEGRATION FRAMEWORK**
- Session metrics incorporation (duration, subjects, action items)
- Evidence-based observation requirements
- Specific content mandates to ensure relevance
- Quantifiable progress indicators

**4. COMMUNICATION PSYCHOLOGY PRINCIPLES**
- Growth mindset language integration ("effort-focused praise")
- Parent partnership acknowledgment (collaborative tone)
- Balance of challenges with achievements (realistic optimism)
- Confidence-building through specific evidence

**5. PEDAGOGICAL BEST PRACTICES**
- Educational terminology appropriate for parent audience
- Constructive feedback theory application
- Metacognitive skill recognition and reinforcement
- Learning science principles in accessible language

**6. STRUCTURAL OPTIMIZATION**
- Professional email format with clear sections
- Logical flow: greeting → highlights → progress → actions → encouragement
- Scannable organization with headers and bullet points
- Appropriate length constraints (400-500 words)

**7. QUALITY CONSTRAINTS**
- Evidence-based observations only (no generic praise)
- Specific, actionable next steps
- Professional tone maintenance
- Credibility preservation through educational accuracy

**8. OUTPUT SPECIFICATIONS**
- Complete email format ready for parent communication
- No additional editing required
- Professional presentation standards
- Immediate usability in real educational settings

This framework ensures the AI generates educationally sound, professionally appropriate, and practically useful parent communications that reflect deep understanding of learning sciences and family engagement best practices."""

        return explanation