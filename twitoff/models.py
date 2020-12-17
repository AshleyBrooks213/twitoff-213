"""SQL Alchemy models and utility functions for Twitoff"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()

MIGRATE = Migrate()


# User Table (in relational database the table is "user")
class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)
    # keeps track of users most recent tweet
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return "<User: {}>".format(self.name)


# Tweet Table (in relational database the table is "tweet")
class Tweet(DB.Model):
    """Tweet Text and Data"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column of character length 500 (unicode)
    text = DB.Column(DB.Unicode(500))
    vect = DB.Column(DB.PickleType, nullable=False)
    # foreign key - user.id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_users():
    """Will get error if ran twice since data already exists"""
    elonmusk = User(id=1, name="elonmusk")
    jackblack = User(id=2, name="jackblack")
    DB.session.add(elonmusk) # adds elonmusk User
    DB.session.add(jackblack) # adds jackblack User
    DB.session.commit() # commits all


#def insert_example_tweets():
    #user1_id = 213
    #user2_id = 330
    #"""Will get error if ran twice since data already exists"""
    #ashleys_tweet1 = Tweet(id=1, text="It's almost Christmas!", user_id=user1_id, user=ashley)
    #travis_tweet1 = Tweet(id=2, text="Hello!", user_id=user2_id, user=travis)
    #ashleys_tweet2 = Tweet(id=3, text="Hola!", user_id=user1_id, user=ashley)
    #travis_tweet2 = Tweet(id=4, text="Hi!", user_id=user2_id, user=travis)
    #ashleys_tweet3 = Tweet(id=5, text="Oui, ca va?", user_id=user1_id, user=ashley)
    #travis_tweet3 = Tweet(id=6, text="Goodbye!", user_id=user2_id, user=travis)
    #DB.session.add(ashleys_tweet1) # adds ashleys_tweet1
    #DB.session.add(travis_tweet1) # adds travis_tweet1
    #DB.session.add(ashleys_tweet2) # adds ashleys_tweet2
    #DB.session.add(travis_tweet2) # adds travis_tweet2
    #DB.session.add(ashleys_tweet3) # adds ashleys_tweet3
    #DB.session.add(travis_tweet3) # adds travis_tweet3
    #DB.session.commit() # commits all

        
        
        

