"""
Tests for Social Network System - Coding Interview Practice

Run specific levels with:
    pytest tests/ -v -k "level1"
    pytest tests/ -v -k "level2"
    pytest tests/ -v -k "level3"
    pytest tests/ -v -k "level4"
"""

import pytest
from social_network import SocialNetwork


@pytest.fixture
def network():
    """Create a fresh SocialNetwork for each test."""
    return SocialNetwork()


# ==================== LEVEL 1: Basic Operations ====================


class TestLevel1BasicOperations:
    """Level 1: Basic user and friendship operations."""

    def test_level1_add_user_success(self, network):
        """Can create a new user."""
        assert network.add_user("alice", "Alice Smith") is True

    def test_level1_add_user_duplicate(self, network):
        """Cannot create duplicate users."""
        network.add_user("alice", "Alice Smith")
        assert network.add_user("alice", "Alice Jones") is False

    def test_level1_add_multiple_users(self, network):
        """Can create multiple different users."""
        assert network.add_user("alice", "Alice") is True
        assert network.add_user("bob", "Bob") is True
        assert network.add_user("charlie", "Charlie") is True

    def test_level1_add_friendship_success(self, network):
        """Can add friendship between two users."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.add_friendship("alice", "bob") is True

    def test_level1_add_friendship_nonexistent_user(self, network):
        """Cannot add friendship if user doesn't exist."""
        network.add_user("alice", "Alice")
        assert network.add_friendship("alice", "bob") is False

    def test_level1_add_friendship_same_user(self, network):
        """Cannot add friendship with oneself."""
        network.add_user("alice", "Alice")
        assert network.add_friendship("alice", "alice") is False

    def test_level1_add_friendship_already_friends(self, network):
        """Cannot add duplicate friendship."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        assert network.add_friendship("alice", "bob") is False
        assert network.add_friendship("bob", "alice") is False  # Bidirectional

    def test_level1_are_friends_true(self, network):
        """are_friends returns True for friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        assert network.are_friends("alice", "bob") is True
        assert network.are_friends("bob", "alice") is True  # Bidirectional

    def test_level1_are_friends_false(self, network):
        """are_friends returns False for non-friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.are_friends("alice", "bob") is False

    def test_level1_are_friends_nonexistent(self, network):
        """are_friends returns False if user doesn't exist."""
        network.add_user("alice", "Alice")
        assert network.are_friends("alice", "bob") is False

    def test_level1_remove_friendship_success(self, network):
        """Can remove existing friendship."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        assert network.remove_friendship("alice", "bob") is True
        assert network.are_friends("alice", "bob") is False

    def test_level1_remove_friendship_bidirectional(self, network):
        """Removing friendship works from either direction."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        assert network.remove_friendship("bob", "alice") is True
        assert network.are_friends("alice", "bob") is False

    def test_level1_remove_friendship_nonexistent(self, network):
        """Cannot remove non-existent friendship."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.remove_friendship("alice", "bob") is False

    def test_level1_readd_friendship_after_removal(self, network):
        """Can re-add friendship after removal."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        network.remove_friendship("alice", "bob")
        assert network.add_friendship("alice", "bob") is True
        assert network.are_friends("alice", "bob") is True


# ==================== LEVEL 2: Query Operations ====================


class TestLevel2QueryOperations:
    """Level 2: Search and relationship analysis."""

    def test_level2_get_friends_empty(self, network):
        """get_friends returns empty for user with no friends."""
        network.add_user("alice", "Alice")
        assert network.get_friends("alice") == []

    def test_level2_get_friends_nonexistent(self, network):
        """get_friends returns empty for non-existent user."""
        assert network.get_friends("alice") == []

    def test_level2_get_friends_single(self, network):
        """get_friends with one friend."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship("alice", "bob")
        assert network.get_friends("alice") == ["bob"]
        assert network.get_friends("bob") == ["alice"]

    def test_level2_get_friends_multiple_sorted(self, network):
        """get_friends returns sorted list."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")
        network.add_friendship("alice", "charlie")
        network.add_friendship("alice", "bob")
        network.add_friendship("alice", "david")
        assert network.get_friends("alice") == ["bob", "charlie", "david"]

    def test_level2_get_mutual_friends_none(self, network):
        """get_mutual_friends with no common friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship("alice", "charlie")
        assert network.get_mutual_friends("alice", "bob") == []

    def test_level2_get_mutual_friends_some(self, network):
        """get_mutual_friends with common friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")
        network.add_friendship("alice", "charlie")
        network.add_friendship("bob", "charlie")
        network.add_friendship("alice", "david")
        network.add_friendship("bob", "david")
        assert network.get_mutual_friends("alice", "bob") == [
            "charlie", "david"]

    def test_level2_get_mutual_friends_nonexistent(self, network):
        """get_mutual_friends returns empty if user doesn't exist."""
        network.add_user("alice", "Alice")
        assert network.get_mutual_friends("alice", "bob") == []

    def test_level2_get_friend_count(self, network):
        """get_friend_count returns correct count."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        assert network.get_friend_count("alice") == 0
        network.add_friendship("alice", "bob")
        assert network.get_friend_count("alice") == 1
        network.add_friendship("alice", "charlie")
        assert network.get_friend_count("alice") == 2

    def test_level2_get_friend_count_nonexistent(self, network):
        """get_friend_count returns 0 for non-existent user."""
        assert network.get_friend_count("alice") == 0

    def test_level2_get_users_by_name_prefix_none(self, network):
        """get_users_by_name_prefix with no matches."""
        network.add_user("alice", "Alice")
        assert network.get_users_by_name_prefix("Bob") == []

    def test_level2_get_users_by_name_prefix_single(self, network):
        """get_users_by_name_prefix with single match."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.get_users_by_name_prefix("Ali") == ["alice"]

    def test_level2_get_users_by_name_prefix_multiple(self, network):
        """get_users_by_name_prefix with multiple matches."""
        network.add_user("user3", "Alice Smith")
        network.add_user("user1", "Alice Jones")
        network.add_user("user2", "Alice Brown")
        network.add_user("user4", "Bob")
        result = network.get_users_by_name_prefix("Alice")
        assert result == ["user1", "user2", "user3"]  # Sorted by user_id

    def test_level2_get_users_by_name_prefix_empty(self, network):
        """get_users_by_name_prefix matches all with empty prefix."""
        network.add_user("bob", "Bob")
        network.add_user("alice", "Alice")
        assert network.get_users_by_name_prefix("") == ["alice", "bob"]


# ==================== LEVEL 3: Time-Based Operations ====================


class TestLevel3TimeBasedOperations:
    """Level 3: Timestamp support for friendships."""

    def test_level3_add_friendship_at_basic(self, network):
        """add_friendship_at creates friendship at timestamp."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.add_friendship_at("alice", "bob", 100) is True
        assert network.are_friends_at("alice", "bob", 100) is True

    def test_level3_add_friendship_at_not_visible_before(self, network):
        """Friendship not visible before its timestamp."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        assert network.are_friends_at("alice", "bob", 99) is False
        assert network.are_friends_at("alice", "bob", 100) is True

    def test_level3_add_friendship_at_invalid(self, network):
        """add_friendship_at returns False for invalid users."""
        network.add_user("alice", "Alice")
        assert network.add_friendship_at("alice", "bob", 100) is False

    def test_level3_remove_friendship_at(self, network):
        """remove_friendship_at removes at timestamp."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        assert network.remove_friendship_at("alice", "bob", 150) is True
        assert network.are_friends_at("alice", "bob", 149) is True
        assert network.are_friends_at("alice", "bob", 150) is False

    def test_level3_remove_friendship_at_nonexistent(self, network):
        """remove_friendship_at returns False if not friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.remove_friendship_at("alice", "bob", 100) is False

    def test_level3_get_friends_at(self, network):
        """get_friends_at returns friends at specific time."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("alice", "charlie", 150)
        assert network.get_friends_at("alice", 99) == []
        assert network.get_friends_at("alice", 100) == ["bob"]
        assert network.get_friends_at("alice", 150) == ["bob", "charlie"]

    def test_level3_get_friends_at_with_removal(self, network):
        """get_friends_at respects removals."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("alice", "charlie", 100)
        network.remove_friendship_at("alice", "bob", 150)
        assert network.get_friends_at("alice", 149) == ["bob", "charlie"]
        assert network.get_friends_at("alice", 150) == ["charlie"]

    def test_level3_get_mutual_friends_at(self, network):
        """get_mutual_friends_at at specific timestamp."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "charlie", 100)
        network.add_friendship_at("bob", "charlie", 150)
        assert network.get_mutual_friends_at("alice", "bob", 100) == []
        assert network.get_mutual_friends_at(
            "alice", "bob", 150) == ["charlie"]

    def test_level3_friendship_duration_simple(self, network):
        """get_friendship_duration for continuous friendship."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        # Friends from 100 onwards, query [100, 200) = 100 time units
        assert network.get_friendship_duration("alice", "bob", 100, 200) == 100

    def test_level3_friendship_duration_partial(self, network):
        """get_friendship_duration when friendship starts mid-interval."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 150)
        # Query [100, 200), friends from 150 = 50 time units
        assert network.get_friendship_duration("alice", "bob", 100, 200) == 50

    def test_level3_friendship_duration_with_removal(self, network):
        """get_friendship_duration with add/remove cycle."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.remove_friendship_at("alice", "bob", 150)
        # Query [0, 200): friends during [100, 150) = 50 time units
        assert network.get_friendship_duration("alice", "bob", 0, 200) == 50

    def test_level3_friendship_duration_multiple_cycles(self, network):
        """get_friendship_duration with multiple add/remove cycles."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.remove_friendship_at("alice", "bob", 150)
        network.add_friendship_at("alice", "bob", 200)
        network.remove_friendship_at("alice", "bob", 250)
        # [100,150) + [200,250) = 50 + 50 = 100 in query [0, 300)
        assert network.get_friendship_duration("alice", "bob", 0, 300) == 100

    def test_level3_friendship_duration_never_friends(self, network):
        """get_friendship_duration when never friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.get_friendship_duration("alice", "bob", 0, 100) == 0

    def test_level3_complex_timeline(self, network):
        """Complex scenario with multiple friendships over time."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")

        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("alice", "charlie", 120)
        network.add_friendship_at("bob", "charlie", 140)
        network.remove_friendship_at("alice", "bob", 160)

        # At 100: alice-bob
        assert network.get_friends_at("alice", 100) == ["bob"]
        # At 130: alice-bob, alice-charlie
        assert network.get_friends_at("alice", 130) == ["bob", "charlie"]
        # At 150: all three connected
        assert network.get_mutual_friends_at(
            "alice", "bob", 150) == ["charlie"]
        # At 170: alice-bob removed
        assert network.get_friends_at("alice", 170) == ["charlie"]
        assert network.are_friends_at("alice", "bob", 170) is False


# ==================== LEVEL 4: Posts & Social Features ====================


class TestLevel4PostsAndSocialFeatures:
    """Level 4: Posts, visibility, and friend recommendations."""

    def test_level4_create_post_success(self, network):
        """Can create a post."""
        network.add_user("alice", "Alice")
        assert network.create_post(
            "alice", "post1", "Hello world!", 100) is True

    def test_level4_create_post_nonexistent_user(self, network):
        """Cannot create post for non-existent user."""
        assert network.create_post("alice", "post1", "Hello!", 100) is False

    def test_level4_create_post_duplicate_id(self, network):
        """Cannot create post with duplicate ID."""
        network.add_user("alice", "Alice")
        network.create_post("alice", "post1", "First", 100)
        assert network.create_post("alice", "post1", "Second", 101) is False

    def test_level4_get_post_author_can_see(self, network):
        """Author can see their own post."""
        network.add_user("alice", "Alice")
        network.create_post("alice", "post1", "Hello!", 100)
        assert network.get_post("post1", "alice", 100) == "Hello!"

    def test_level4_get_post_friend_can_see(self, network):
        """Friend can see post."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.create_post("alice", "post1", "Hello!", 100)
        assert network.get_post("post1", "bob", 100) == "Hello!"

    def test_level4_get_post_non_friend_cannot_see(self, network):
        """Non-friend cannot see post."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.create_post("alice", "post1", "Hello!", 100)
        assert network.get_post("post1", "bob", 100) is None

    def test_level4_get_post_friend_before_friendship(self, network):
        """Cannot see post before becoming friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 150)
        network.create_post("alice", "post1", "Hello!", 100)
        assert network.get_post("post1", "bob", 100) is None
        assert network.get_post("post1", "bob", 150) == "Hello!"

    def test_level4_get_post_nonexistent(self, network):
        """get_post returns None for non-existent post."""
        network.add_user("alice", "Alice")
        assert network.get_post("post1", "alice", 100) is None

    def test_level4_get_feed_own_posts(self, network):
        """Feed includes own posts."""
        network.add_user("alice", "Alice")
        network.create_post("alice", "post1", "First", 100)
        network.create_post("alice", "post2", "Second", 200)
        # Most recent first
        assert network.get_feed("alice", 200) == ["post2", "post1"]

    def test_level4_get_feed_friend_posts(self, network):
        """Feed includes friends' posts."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.create_post("alice", "post1", "Alice's post", 100)
        network.create_post("bob", "post2", "Bob's post", 150)
        # Bob's feed at 150 includes both
        feed = network.get_feed("bob", 150)
        assert feed == ["post2", "post1"]

    def test_level4_get_feed_sorted_by_time(self, network):
        """Feed sorted by creation time, most recent first."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("alice", "charlie", 100)
        network.create_post("bob", "post1", "B1", 100)
        network.create_post("charlie", "post2", "C1", 150)
        network.create_post("bob", "post3", "B2", 200)
        network.create_post("alice", "post4", "A1", 250)
        assert network.get_feed("alice", 250) == [
            "post4", "post3", "post2", "post1"]

    def test_level4_block_user_success(self, network):
        """Can block another user."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        assert network.block_user("alice", "bob", 100) is True

    def test_level4_block_user_invalid(self, network):
        """Cannot block non-existent user."""
        network.add_user("alice", "Alice")
        assert network.block_user("alice", "bob", 100) is False

    def test_level4_block_user_already_blocked(self, network):
        """Cannot block already blocked user."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.block_user("alice", "bob", 100)
        assert network.block_user("alice", "bob", 150) is False

    def test_level4_blocked_user_cannot_see_posts(self, network):
        """Blocked user cannot see blocker's posts."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.create_post("alice", "post1", "Hello!", 100)
        # Before block, bob can see
        assert network.get_post("post1", "bob", 100) == "Hello!"
        # After block, bob cannot see
        network.block_user("alice", "bob", 150)
        assert network.get_post("post1", "bob", 150) is None

    def test_level4_blocker_can_still_see_blocked_posts(self, network):
        """Blocker can still see blocked user's posts (asymmetric)."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        network.create_post("bob", "post1", "Bob's post", 100)
        network.block_user("alice", "bob", 150)
        # Alice (blocker) can still see Bob's posts
        assert network.get_post("post1", "alice", 150) == "Bob's post"

    def test_level4_get_friend_recommendations_basic(self, network):
        """Basic friend recommendations (friends of friends)."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("bob", "charlie", 100)
        # Alice's recommendations: charlie (friend of bob)
        assert network.get_friend_recommendations("alice", 100) == ["charlie"]

    def test_level4_get_friend_recommendations_excludes_friends(self, network):
        """Recommendations exclude existing friends."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("bob", "charlie", 100)
        network.add_friendship_at("alice", "charlie", 100)
        # Alice already friends with charlie
        assert network.get_friend_recommendations("alice", 100) == []

    def test_level4_get_friend_recommendations_sorted_by_mutual(self, network):
        """Recommendations sorted by mutual friend count."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")
        network.add_user("eve", "Eve")
        # Alice friends with bob and charlie
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("alice", "charlie", 100)
        # David friends with both bob and charlie (2 mutual with alice)
        network.add_friendship_at("bob", "david", 100)
        network.add_friendship_at("charlie", "david", 100)
        # Eve friends with only bob (1 mutual with alice)
        network.add_friendship_at("bob", "eve", 100)
        # David should be first (2 mutual), then eve (1 mutual)
        assert network.get_friend_recommendations("alice", 100) == [
            "david", "eve"]

    def test_level4_get_friend_recommendations_limit_5(self, network):
        """Recommendations limited to top 5."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_friendship_at("alice", "bob", 100)
        # Create 10 friends of bob
        for i in range(10):
            uid = f"user{i:02d}"
            network.add_user(uid, f"User {i}")
            network.add_friendship_at("bob", uid, 100)
        recs = network.get_friend_recommendations("alice", 100)
        assert len(recs) == 5

    def test_level4_get_friend_recommendations_excludes_blocked(self, network):
        """Recommendations exclude blocked users (both directions)."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("bob", "charlie", 100)
        network.add_friendship_at("bob", "david", 100)
        # Alice blocks charlie
        network.block_user("alice", "charlie", 100)
        # David blocks alice
        network.block_user("david", "alice", 100)
        # Neither should be recommended
        assert network.get_friend_recommendations("alice", 100) == []

    def test_level4_get_friend_recommendations_tiebreak_by_userid(self, network):
        """Recommendations with same mutual count sorted by user_id."""
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("zack", "Zack")
        network.add_user("charlie", "Charlie")
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("bob", "zack", 100)
        network.add_friendship_at("bob", "charlie", 100)
        # Both have 1 mutual friend, sorted by user_id
        assert network.get_friend_recommendations("alice", 100) == [
            "charlie", "zack"]

    def test_level4_complex_scenario(self, network):
        """Complex scenario with posts, blocks, and recommendations."""
        # Setup users
        network.add_user("alice", "Alice")
        network.add_user("bob", "Bob")
        network.add_user("charlie", "Charlie")
        network.add_user("david", "David")

        # Friendships
        network.add_friendship_at("alice", "bob", 100)
        network.add_friendship_at("bob", "charlie", 100)
        network.add_friendship_at("charlie", "david", 100)

        # Posts
        network.create_post("alice", "p1", "Alice post", 100)
        network.create_post("bob", "p2", "Bob post", 110)
        network.create_post("charlie", "p3", "Charlie post", 120)

        # At 120: Alice can see p1 (own), p2 (friend bob)
        alice_feed = network.get_feed("alice", 120)
        assert "p1" in alice_feed
        assert "p2" in alice_feed
        assert "p3" not in alice_feed  # charlie not friend of alice

        # Recommendations for alice: charlie (friend of bob)
        assert network.get_friend_recommendations("alice", 120) == ["charlie"]

        # Block charlie
        network.block_user("alice", "charlie", 130)
        assert network.get_friend_recommendations("alice", 130) == []
