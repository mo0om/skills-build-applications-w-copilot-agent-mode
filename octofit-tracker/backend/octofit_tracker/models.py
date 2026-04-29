from djongo import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    members = models.ArrayReferenceField(to=UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.FloatField(help_text="Duration in minutes")
    distance = models.FloatField(help_text="Distance in kilometers", blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.FloatField()
    rank = models.IntegerField()
    week = models.IntegerField()
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.username} - {self.score}"

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - Suggestion"
