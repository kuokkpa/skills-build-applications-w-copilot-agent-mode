from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (passwords are temporary test-only values and should not be used in production)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='Ir0nM@n_T3st!', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='C@pt@in_T3st!', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='B@tm@n_T3st!', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='Sup3rm@n_T3st!', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=captain, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=25)
        Activity.objects.create(user=superman, type='run', duration=50)

        # Create workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Workout.objects.create(name='Strength Builder', description='Full body strength workout')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=captain, points=90)
        Leaderboard.objects.create(user=batman, points=95)
        Leaderboard.objects.create(user=superman, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
