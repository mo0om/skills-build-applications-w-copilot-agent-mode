from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Sample data
        users = [
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "captain@marvel.com", "team": "marvel"},
            {"name": "Natasha Romanoff", "email": "blackwidow@marvel.com", "team": "marvel"},
        ]
        db.users.insert_many(users)

        teams = [
            {"name": "marvel", "members": ["Tony Stark", "Steve Rogers", "Natasha Romanoff"]},
            {"name": "dc", "members": ["Clark Kent", "Bruce Wayne", "Diana Prince"]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"user": "Clark Kent", "activity": "Flight", "duration": 60},
            {"user": "Bruce Wayne", "activity": "Martial Arts", "duration": 45},
            {"user": "Tony Stark", "activity": "Engineering", "duration": 120},
            {"user": "Steve Rogers", "activity": "Running", "duration": 30},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"team": "marvel", "points": 250},
            {"team": "dc", "points": 200},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"user": "Clark Kent", "workout": "Bench Press", "weight": 1000},
            {"user": "Tony Stark", "workout": "Cardio", "weight": 0},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
