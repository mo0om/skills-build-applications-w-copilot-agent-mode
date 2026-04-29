from django.test import TestCase
from .models import UserProfile, Team, Activity, LeaderboardEntry, WorkoutSuggestion

class UserProfileModelTest(TestCase):
    def test_create_user_profile(self):
        user = UserProfile.objects.create(user_id='u1', username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = UserProfile.objects.create(user_id='u2', username='member', email='member@example.com')
        team = Team.objects.create(name='TeamA')
        team.members.add(user)
        self.assertEqual(team.name, 'TeamA')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = UserProfile.objects.create(user_id='u3', username='active', email='active@example.com')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30)
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = UserProfile.objects.create(user_id='u4', username='leader', email='leader@example.com')
        entry = LeaderboardEntry.objects.create(user=user, score=100, rank=1, week=17, year=2026)
        self.assertEqual(entry.rank, 1)

class WorkoutSuggestionModelTest(TestCase):
    def test_create_workout_suggestion(self):
        user = UserProfile.objects.create(user_id='u5', username='suggest', email='suggest@example.com')
        suggestion = WorkoutSuggestion.objects.create(user=user, suggestion='Try HIIT')
        self.assertEqual(suggestion.suggestion, 'Try HIIT')
