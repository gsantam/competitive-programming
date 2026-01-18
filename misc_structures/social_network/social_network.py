"""
Social Network System - Coding Interview Practice

Implement the methods below according to the specifications in README.md.
Progress through the 4 levels, implementing each set of methods.

Run tests with: pytest tests/ -v -k "levelX" (where X is 1-4)
"""
from collections import defaultdict
from bisect import insort, bisect


class Person:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = {}
        self.friends_log = {}
        self.posts = []
        self.blocks = []

    def add_friend(self, person):
        self.friends[person.user_id] = person

    def add_friend_to_log(self, person, timestamp):
        if person.user_id not in self.friends_log:
            self.friends_log[person.user_id] = []
        insort(self.friends_log[person.user_id], [timestamp, person, "add"])

    def remove_friend_to_log(self, person, timestamp):
        insort(self.friends_log[person.user_id], [timestamp, person, "rem"])

    def remove_friend(self, user_id):
        self.friends.pop(user_id, None)


class SocialNetwork:
    def __init__(self):
        self.network = dict()
        self.posts = dict()
        self.internal_counter = 10**5

    # ==================== LEVEL 1: Basic Operations ====================

    def add_user(self, user_id: str, name: str) -> bool:
        """
        Creates a new user with the given ID and name.
        Returns True if successful, False if user already exists.
        """
        if user_id in self.network:
            return False
        self.network[user_id] = Person(user_id, name)
        return True

    def add_friendship(self, user_id1: str, user_id2: str) -> bool:
        self.internal_counter += 1
        return self.add_friendship_at(user_id1, user_id2, self.internal_counter)

    def remove_friendship(self, user_id1: str, user_id2: str) -> bool:
        """
        Removes the friendship between two users.
        Returns True if successful, False if friendship doesn't exist.
        """
        self.internal_counter += 1
        return self.remove_friendship_at(user_id1, user_id2, self.internal_counter)

    def are_friends(self, user_id1: str, user_id2: str) -> bool:
        """
        Returns True if the two users are friends, False otherwise.
        """
        self.internal_counter += 1
        return self.are_friends_at(user_id1, user_id2, self.internal_counter)

    # ==================== LEVEL 2: Query Operations ====================

    def get_friends(self, user_id: str) -> list[str]:
        """
        Returns list of friend user_ids, sorted lexicographically.
        Empty list if user doesn't exist or has no friends.
        """
        self.internal_counter += 1
        return self.get_friends_at(user_id, self.internal_counter)

    def get_mutual_friends(self, user_id1: str, user_id2: str) -> list[str]:
        """
        Returns list of users who are friends with BOTH users.
        Sorted lexicographically. Empty list if either user doesn't exist.
        """
        self.internal_counter += 1
        return self.get_mutual_friends_at(user_id1, user_id2, self.internal_counter)

    def get_friend_count(self, user_id: str) -> int:
        """
        Returns the number of friends. 0 if user doesn't exist.
        """
        return len(self.get_friends(user_id))

    def get_users_by_name_prefix(self, prefix: str) -> list[str]:
        """
        Returns user_ids whose names start with prefix.
        Sorted lexicographically by user_id.
        """
        user_ids = list(self.network.keys())
        user_ids = [
            user_id for user_id in user_ids if self.network[user_id].name.startswith(prefix)]
        return sorted(user_ids)
    # ==================== LEVEL 3: Time-Based Operations ====================

    def add_friendship_at(
        self, user_id1: str, user_id2: str, timestamp: int
    ) -> bool:
        """
        Creates friendship at a specific timestamp.
        Returns True if successful, False otherwise.
        """
        if user_id1 == user_id2:
            return False
        if user_id1 in self.network and user_id2 in self.network:
            if self.are_friends_at(user_id1, user_id2, timestamp):
                return False
            self.network[user_id1].add_friend_to_log(
                self.network[user_id2], timestamp)
            self.network[user_id2].add_friend_to_log(
                self.network[user_id1], timestamp)
            return True
        return False

    def remove_friendship_at(
        self, user_id1: str, user_id2: str, timestamp: int
    ) -> bool:
        """
        Removes friendship at a specific timestamp.
        Returns True if successful, False otherwise.
        """
        if self.are_friends_at(user_id1, user_id2, timestamp):
            self.network[user_id1].remove_friend_to_log(
                self.network[user_id2], timestamp)
            self.network[user_id2].remove_friend_to_log(
                self.network[user_id1], timestamp)
            return True
        return False

    def are_friends_at(
        self, user_id1: str, user_id2: str, timestamp: int
    ) -> bool:
        """
        Returns whether users were friends at the given timestamp.
        """
        if user_id1 in self.network and user_id2 in self.network:
            if user_id2 in self.network[user_id1].friends_log:
                friend_log = sorted(
                    self.network[user_id1].friends_log[user_id2])
                for i in range(len(friend_log)):
                    ts, _, action = friend_log[i]
                    if timestamp >= ts and (i == len(friend_log) - 1 or friend_log[i+1][0] > timestamp):
                        if action == "add":
                            return True
        return False

    def get_friends_at(self, user_id: str, timestamp: int) -> list[str]:
        """
        Returns list of friends at the given timestamp.
        Sorted lexicographically.
        """
        friend_ids = []
        if user_id in self.network:
            for friend_user_id in self.network[user_id].friends_log:
                if self.are_friends_at(user_id, friend_user_id, timestamp):
                    if not self.is_user_block(friend_user_id, user_id, timestamp):
                        friend_ids.append(friend_user_id)
        return sorted(friend_ids)

    def get_mutual_friends_at(
        self, user_id1: str, user_id2: str, timestamp: int
    ) -> list[str]:
        friends_1 = self.get_friends_at(user_id1, timestamp)
        friends_2 = self.get_friends_at(user_id2, timestamp)
        return sorted(list(set(friends_1).intersection(set(friends_2))))

    def get_friendship_duration(
        self, user_id1: str, user_id2: str, start_time: int, end_time: int
    ) -> int:
        """
        Returns total time units the users were friends during [start_time, end_time).
        Accounts for multiple add/remove cycles.
        """
        total = 0
        if user_id1 not in self.network:
            return 0
        if user_id2 not in self.network[user_id1].friends_log:
            return 0
        frienship_log = self.network[user_id1].friends_log[user_id2]
        if len(frienship_log) == 0:
            return 0
        frienship_log_added = frienship_log+[[10**10, None, None]]
        for i, (timestamp, _, action) in enumerate(frienship_log_added):
            if action == "add":
                start_int = max(timestamp, start_time)
                if i < len(frienship_log_added)-1:
                    end_int = min(end_time, frienship_log_added[i+1][0])
                    seg_time = max(end_int-start_int, 0)
                    total += seg_time
        return total

    # ==================== LEVEL 4: Posts & Social Features ====================

    def create_post(
        self, user_id: str, post_id: str, content: str, timestamp: int
    ) -> bool:
        """
        Creates a post by the user at the given timestamp.
        Returns True if successful, False if user/post invalid.
        """
        if user_id not in self.network:
            return False

        if post_id in self.posts:
            return False
        self.network[user_id].posts.append(post_id)
        self.posts[post_id] = [timestamp, user_id, content, post_id]

        return True

    def get_post(
        self, post_id: str, viewer_id: str, timestamp: int
    ) -> str | None:
        """
        Returns post content if viewer can see it at timestamp.
        Viewer can see if they're the author or friends with author.
        Returns None if not visible or doesn't exist.
        """
        if post_id not in self.posts:
            return None
        post_log = self.posts[post_id]
        if post_log[0] > timestamp:
            return None
        user_id = post_log[1]
        content = post_log[2]
        if user_id == viewer_id:
            return content
        friends = set(self.get_friends_at(viewer_id, timestamp))
        if user_id in friends and not self.is_user_block(user_id, viewer_id, timestamp):
            return content
        return None

    def get_own_posts(self, user_id, timestamp):
        if user_id not in self.network:
            return []
        my_posts = self.network[user_id].posts
        visible_posts = []
        for my_post in my_posts:
            if self.posts[my_post][0] <= timestamp:
                visible_posts.append(self.posts[my_post])
        return visible_posts

    def get_feed(self, user_id: str, timestamp: int) -> list[str]:
        """
        Returns post_ids visible to user at timestamp.
        Sorted by creation time (most recent first).
        Includes own posts and friends' posts.
        """
        my_posts = self.get_own_posts(user_id, timestamp)
        my_friends = self.get_friends_at(user_id, timestamp)
        for friend_id in my_friends:
            my_posts += self.get_own_posts(friend_id, timestamp)
        my_posts = sorted(my_posts, reverse=True)
        return [x[3] for x in my_posts]

    def is_user_block(
        self, blocker_id: str, blocked_id: str, timestamp: int
    ) -> bool:
        blocks = self.network[blocker_id].blocks
        for ts, user_id in blocks:
            if user_id == blocked_id and timestamp >= ts:
                return True
        return False

    def block_user(
        self, blocker_id: str, blocked_id: str, timestamp: int
    ) -> bool:
        """
        blocker_id blocks blocked_id starting at timestamp.
        Blocking is NOT bidirectional.
        Returns True if successful, False otherwise.
        """
        if blocker_id not in self.network:
            return False
        if blocked_id not in self.network:
            return False
        if self.is_user_block(blocker_id, blocked_id, timestamp):
            return False
        self.network[blocker_id].blocks.append([timestamp, blocked_id])
        return True

    def get_friend_recommendations(
        self, user_id: str, timestamp: int
    ) -> list[str]:
        """
        Returns recommended friends (friends of friends).
        Excludes current friends and blocked users (either direction).
        Sorted by mutual friend count (desc), then user_id (asc).
        Limited to top 5.
        """
        user_friends = self.get_friends_at(user_id, timestamp)
        user_friends = set([user_friend_id for user_friend_id in user_friends if not self.is_user_block(
            user_id, user_friend_id, timestamp) and not self.is_user_block(user_friend_id, user_id, timestamp)])
        recommendations_mutual = defaultdict(lambda: 0)
        for user_friend_id in user_friends:
            user_friend_friend_ids = self.get_friends_at(
                user_friend_id, timestamp)
            user_friend_friend_ids = [user_friend_friend_id for user_friend_friend_id in user_friend_friend_ids if not self.is_user_block(
                user_id, user_friend_friend_id, timestamp) and not self.is_user_block(user_friend_friend_id, user_id, timestamp) and user_friend_friend_id not in user_friends and user_friend_friend_id != user_id]
            for user_friend_friend_id in user_friend_friend_ids:
                recommendations_mutual[user_friend_friend_id] += 1
        recommendations_mutual = sorted([
            [-recommendations_mutual[user_id], user_id] for user_id in recommendations_mutual])
        return [x[1] for x in recommendations_mutual][:5]
