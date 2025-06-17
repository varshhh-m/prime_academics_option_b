
import re
import json
from typing import Dict, List, Any
from datetime import datetime

class EducationalTranscriptAnalyzer:
   
    
    def __init__(self):
        self.educational_patterns = {
            'subjects': {
                'mathematics': ['math', 'ratio', 'median', 'formula', 'calculator', 'equation', 'algebra', 'geometry'],
                'reading': ['reading', 'comprehension', 'kaplan', 'passage', 'section'],
                'science': ['physics', 'chemistry', 'biology', 'force', 'formula'],
                'test_prep': ['test', 'exam', 'preparation', 'score', 'practice']
            },
            'learning_indicators': {
                'understanding': ['makes sense', 'oh yeah', 'i see', 'got it', 'understand', 'that works'],
                'confusion': ['don\'t understand', 'confused', 'what', 'huh', 'wrong', 'not working'],
                'effort': ['trying', 'working on', 'practicing', 'studying', 'i think'],
                'confidence': ['i know', 'sure', 'confident', 'definitely', 'right']
            },
            'teaching_strategies': {
                'scaffolding': ['let me help', 'step by step', 'break it down', 'think about it'],
                'questioning': ['what do you think', 'how would you', 'why', 'can you help'],
                'feedback': ['good job', 'well done', 'that\'s right', 'not quite', 'correct'],
                'encouragement': ['you can do it', 'keep trying', 'almost there', 'good']
            }
        }
    
    def analyze_transcript(self, transcript_text: str) -> Dict[str, Any]:
        
        
        print(" Analyzing transcript with educational expertise...")
        
        
        parsed_conversations = self._parse_conversations(transcript_text)
        
        
        session_metadata = self._extract_session_metadata(transcript_text)
        
        
        subject_analysis = self._analyze_subjects(transcript_text)
        learning_patterns = self._analyze_learning_patterns(parsed_conversations)
        teaching_strategies = self._analyze_teaching_strategies(parsed_conversations)
        
       
        student_condition = self._assess_student_condition(parsed_conversations, transcript_text)
        
      
        action_items = self._extract_action_items(transcript_text)
        
       
        performance_indicators = self._analyze_academic_performance(parsed_conversations)
        
        
        educational_insights = self._generate_educational_insights(
            subject_analysis, learning_patterns, student_condition
        )
        
        result = {
            'session_metadata': session_metadata,
            'subject_analysis': subject_analysis,
            'learning_patterns': learning_patterns,
            'teaching_strategies': teaching_strategies,
            'student_condition': student_condition,
            'action_items': action_items,
            'performance_indicators': performance_indicators,
            'educational_insights': educational_insights,
            'parsed_conversations': parsed_conversations
        }
        
        print(f" Analysis complete - {len(parsed_conversations)} conversation segments analyzed")
        print(f"    Subjects identified: {', '.join(subject_analysis.get('subjects_identified', []))}")
        print(f"    Action items found: {len(action_items)}")
        print(f"    Teaching moments: {len(teaching_strategies.get('teaching_moments', []))}")
        
        return result
    
    def _parse_conversations(self, text: str) -> List[Dict[str, Any]]:
        
        conversations = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            match = re.match(r'(\d+:\d+)\s*-\s*(student|tutor)', line, re.IGNORECASE)
            if match:
                timestamp = match.group(1)
                speaker = match.group(2).lower()
                
                
                content_start = line.lower().find(speaker) + len(speaker)
                speech_content = line[content_start:].strip()
                if speech_content.startswith('-'):
                    speech_content = speech_content[1:].strip()
                
                conversations.append({
                    'timestamp': timestamp,
                    'speaker': speaker,
                    'content': speech_content,
                    'word_count': len(speech_content.split()) if speech_content else 0,
                    'educational_markers': self._identify_educational_markers(speech_content)
                })
        
        return conversations
    
    def _extract_session_metadata(self, text: str) -> Dict[str, Any]:
        
        metadata = {}
        
        
        duration_match = re.search(r'Duration:\s*(\d+)\s*minutes', text, re.IGNORECASE)
        if duration_match:
            metadata['duration_minutes'] = int(duration_match.group(1))
        
       
        if 'test preparation' in text.lower():
            metadata['session_type'] = 'Test Preparation'
            metadata['urgency_level'] = 'High'
        
        if 'day before test' in text.lower():
            metadata['timing_context'] = 'Final preparation session'
            metadata['pressure_level'] = 'High'
        
        
        action_count = len(re.findall(r'ACTION ITEM:', text))
        metadata['action_items_count'] = action_count
        
        return metadata
    
    def _analyze_subjects(self, text: str) -> Dict[str, Any]:
        
        text_lower = text.lower()
        subjects_found = {}
        
        for subject, keywords in self.educational_patterns['subjects'].items():
            matches = sum(1 for keyword in keywords if keyword in text_lower)
            if matches > 0:
                subjects_found[subject] = {
                    'keyword_matches': matches,
                    'prominence': 'high' if matches > 5 else 'medium' if matches > 2 else 'low'
                }
        
      
        math_topics = []
        if 'mathematics' in subjects_found:
            if 'ratio' in text_lower: math_topics.append('Ratios and Proportions')
            if 'median' in text_lower: math_topics.append('Statistics and Data Analysis')
            if 'histogram' in text_lower: math_topics.append('Data Visualization')
            if 'formula' in text_lower: math_topics.append('Formula Application')
            if 'calculator' in text_lower: math_topics.append('Computational Skills')
        
        return {
            'subjects_identified': list(subjects_found.keys()),
            'subject_details': subjects_found,
            'mathematics_topics': math_topics,
            'primary_focus': max(subjects_found.keys(), key=lambda x: subjects_found[x]['keyword_matches']) if subjects_found else None
        }
    
    def _analyze_learning_patterns(self, conversations: List[Dict]) -> Dict[str, Any]:
        
        student_conversations = [c for c in conversations if c['speaker'] == 'student']
        
        learning_indicators = {
            'understanding_moments': 0,
            'confusion_moments': 0,
            'effort_indicators': 0,
            'confidence_markers': 0
        }
        
        specific_moments = []
        
        for conv in student_conversations:
            content_lower = conv['content'].lower()
            
            
            for indicator_type, keywords in self.educational_patterns['learning_indicators'].items():
                for keyword in keywords:
                    if keyword in content_lower:
                        learning_indicators[f'{indicator_type}_moments'] += 1
                        specific_moments.append({
                            'timestamp': conv['timestamp'],
                            'type': indicator_type,
                            'context': conv['content'][:80] + "..." if len(conv['content']) > 80 else conv['content']
                        })
        
        
        total_words = sum(c['word_count'] for c in student_conversations)
        avg_response_length = total_words / len(student_conversations) if student_conversations else 0
        
        engagement_level = 'high' if avg_response_length > 12 else 'medium' if avg_response_length > 6 else 'low'
        
        return {
            'learning_indicators': learning_indicators,
            'specific_moments': specific_moments,
            'engagement_level': engagement_level,
            'average_response_length': avg_response_length,
            'total_student_responses': len(student_conversations)
        }
    
    def _analyze_teaching_strategies(self, conversations: List[Dict]) -> Dict[str, Any]:
        
        tutor_conversations = [c for c in conversations if c['speaker'] == 'tutor']
        
        strategy_usage = {
            'scaffolding': 0,
            'questioning': 0,
            'feedback': 0,
            'encouragement': 0
        }
        
        teaching_moments = []
        
        for conv in tutor_conversations:
            content_lower = conv['content'].lower()
            
            
            for strategy, keywords in self.educational_patterns['teaching_strategies'].items():
                for keyword in keywords:
                    if keyword in content_lower:
                        strategy_usage[strategy] += 1
            
            
            if any(phrase in content_lower for phrase in ['think about it again', 'try this', 'let me explain']):
                teaching_moments.append({
                    'timestamp': conv['timestamp'],
                    'strategy': 'Error Correction',
                    'approach': 'Guided redirection'
                })
            
            if any(phrase in content_lower for phrase in ['what do you think', 'how would you', 'why']):
                teaching_moments.append({
                    'timestamp': conv['timestamp'],
                    'strategy': 'Socratic Questioning',
                    'approach': 'Concept exploration'
                })
        
        return {
            'strategy_distribution': strategy_usage,
            'teaching_moments': teaching_moments,
            'dominant_approach': max(strategy_usage.keys(), key=lambda x: strategy_usage[x]) if any(strategy_usage.values()) else 'balanced',
            'total_teaching_interventions': len(teaching_moments)
        }
    
    def _assess_student_condition(self, conversations: List[Dict], full_text: str) -> Dict[str, Any]:
        
        student_content = " ".join([c['content'] for c in conversations if c['speaker'] == 'student']).lower()
        
        condition = {
            'health_status': 'normal',
            'emotional_state': 'stable',
            'engagement_level': 'moderate',
            'confidence_level': 'developing',
            'stress_indicators': []
        }
        
        
        if any(word in student_content for word in ['sick', 'doctor', 'steroids', 'inhalers']):
            condition['health_status'] = 'recently_ill_but_attending'
        
       
        response_count = len([c for c in conversations if c['speaker'] == 'student'])
        if response_count > 25:
            condition['engagement_level'] = 'high'
        elif response_count > 15:
            condition['engagement_level'] = 'medium'
        else:
            condition['engagement_level'] = 'low'
        
       
        if any(phrase in student_content for phrase in ['makes sense', 'got it', 'understand']):
            condition['confidence_level'] = 'building'
        
        if any(phrase in student_content for phrase in ['don\'t know', 'confused', 'wrong']):
            condition['stress_indicators'].append('self_doubt')
        
        
        if 'workout' in student_content and condition['health_status'] == 'recently_ill_but_attending':
            condition['resilience_level'] = 'high'
        
        return condition
    
    def _extract_action_items(self, text: str) -> List[Dict[str, Any]]:
        
        action_items = []
        lines = text.split('\n')
        
        for line in lines:
            if 'ACTION ITEM:' in line:
                description = line.split('ACTION ITEM:')[1].strip()
                category = self._categorize_action_item(description)
                priority = self._assess_action_priority(description)
                
                action_items.append({
                    'description': description,
                    'category': category,
                    'priority': priority,
                    'type': 'Academic' if 'practice' in description.lower() or 'review' in description.lower() else 'Logistical'
                })
        
        return action_items
    
    def _categorize_action_item(self, description: str) -> str:
        
        desc_lower = description.lower()
        
        if any(word in desc_lower for word in ['practice', 'review', 'study', 'kaplan']):
            return 'Academic Preparation'
        elif any(word in desc_lower for word in ['wake up', 'leave', 'time']):
            return 'Test Day Logistics'
        elif any(word in desc_lower for word in ['charge', 'lay out', 'prepare']):
            return 'Material Organization'
        else:
            return 'General Support'
    
    def _assess_action_priority(self, description: str) -> str:
        
        desc_lower = description.lower()
        
        if any(word in desc_lower for word in ['test tomorrow', 'wake up', 'leave house']):
            return 'Critical'
        elif any(word in desc_lower for word in ['practice', 'review']):
            return 'High'
        else:
            return 'Medium'
    
    def _analyze_academic_performance(self, conversations: List[Dict]) -> Dict[str, Any]:
       
        all_content = " ".join([c['content'] for c in conversations]).lower()
        
        performance = {
            'error_patterns': [],
            'strength_areas': [],
            'improvement_opportunities': [],
            'conceptual_understanding': 'developing'
        }
        
        
        if 'calculator' in all_content and 'wrong' in all_content:
            performance['error_patterns'].append('Calculator input errors')
        
        if 'time' in all_content and 'running out' in all_content:
            performance['error_patterns'].append('Time management challenges')
        
        if 'well done' in all_content:
            performance['strength_areas'].append('Problem-solving accuracy')
        
        if 'makes sense' in all_content:
            performance['strength_areas'].append('Conceptual understanding')
        
       
        if len(performance['error_patterns']) > 0:
            performance['improvement_opportunities'].append('Strategic execution refinement')
        
        return performance
    
    def _generate_educational_insights(self, subject_analysis: Dict, learning_patterns: Dict, student_condition: Dict) -> Dict[str, Any]:
        
        insights = {
            'session_effectiveness': 'positive',
            'learning_trajectory': 'upward',
            'key_themes': [],
            'pedagogical_recommendations': []
        }
        
        
        understanding = learning_patterns['learning_indicators']['understanding_moments']
        confusion = learning_patterns['learning_indicators']['confusion_moments']
        
        if understanding > confusion:
            insights['session_effectiveness'] = 'high'
            insights['key_themes'].append('Strong conceptual progress')
        
        
        if student_condition['engagement_level'] in ['high', 'medium'] and student_condition['confidence_level'] == 'building':
            insights['learning_trajectory'] = 'positive'
        
        
        if subject_analysis['primary_focus'] == 'mathematics':
            insights['pedagogical_recommendations'].append('Continue systematic mathematical problem-solving approach')
        
        if student_condition['health_status'] == 'recently_ill_but_attending':
            insights['pedagogical_recommendations'].append('Acknowledge resilience and maintain confidence building')
        
        return insights
    
    def _identify_educational_markers(self, content: str) -> List[str]:
        
        markers = []
        content_lower = content.lower()
        
        if any(word in content_lower for word in ['understand', 'makes sense']):
            markers.append('comprehension')
        if any(word in content_lower for word in ['confused', 'don\'t get']):
            markers.append('confusion')
        if any(word in content_lower for word in ['practice', 'study']):
            markers.append('academic_preparation')
        
        return markers


if __name__ == "__main__":
    analyzer = EducationalTranscriptAnalyzer()
    
   
    sample_text = """
    SESSION DETAILS:
    * Duration: 63 minutes
    
    0:00 - student
    Sorry, 2.45, but I'm definitely wrong.
    
    0:02 - tutor
    Sorry. Totally fine. I'm happy to add a little time with you.
    
    ACTION ITEM: Complete 1 Kaplan reading section on computer (30 min)
    """
    
    result = analyzer.analyze_transcript(sample_text)
    print(f" Test completed - found {len(result['parsed_conversations'])} conversations")
