# Social Network System - Coding Interview Practice

## Overview

This is a practice coding interview similar to the Anthropic CodeSignal assessment. You'll implement a social network system managing users, friendships, and posts. The challenge involves bidirectional relationships and graph traversal.

**Time Limit:** 90 minutes (simulating the real test)

**Goal:** Progress through all 4 levels, passing all tests at each level before moving to the next.

---

## Level 1: Basic User & Friendship Operations

Implement fundamental operations for users and friendships. **Friendships are bidirectional** — if A is friends with B, then B is friends with A.

### Methods to Implement:

- **`add_user(user_id: str, name: str) -> bool`**  
  Creates a new user with the given ID and name. Returns `True` if successful, `False` if user already exists.

- **`add_friendship(user_id1: str, user_id2: str) -> bool`**  
  Creates a bidirectional friendship between two users. Returns `True` if successful. Returns `False` if either user doesn't exist, they're the same user, or they're already friends.

- **`remove_friendship(user_id1: str, user_id2: str) -> bool`**  
  Removes the friendship between two users. Returns `True` if successful, `False` if the friendship doesn't exist.

- **`are_friends(user_id1: str, user_id2: str) -> bool`**  
  Returns `True` if the two users are friends, `False` otherwise.

---

## Level 2: Query Operations

Add search and relationship analysis capabilities.

### Methods to Implement:

- **`get_friends(user_id: str) -> list[str]`**  
  Returns a list of user IDs who are friends with the given user, sorted lexicographically. Returns empty list if user doesn't exist or has no friends.

- **`get_mutual_friends(user_id1: str, user_id2: str) -> list[str]`**  
  Returns a list of user IDs who are friends with BOTH users, sorted lexicographically. Returns empty list if either user doesn't exist.

- **`get_friend_count(user_id: str) -> int`**  
  Returns the number of friends the user has. Returns 0 if user doesn't exist.

- **`get_users_by_name_prefix(prefix: str) -> list[str]`**  
  Returns a list of user IDs whose names start with the given prefix, sorted lexicographically by user_id.

---

## Level 3: Time-Based Operations

Add timestamp support for tracking when friendships were formed and querying historical state.

### Important Notes:
- All timestamps are integers representing time units.
- Friendships take effect at the specified timestamp.
- When querying at a timestamp, only friendships that exist at that time are considered.

### Methods to Implement:

- **`add_friendship_at(user_id1: str, user_id2: str, timestamp: int) -> bool`**  
  Same as `add_friendship`, but the friendship takes effect at the given timestamp.

- **`remove_friendship_at(user_id1: str, user_id2: str, timestamp: int) -> bool`**  
  Same as `remove_friendship`, but the removal takes effect at the given timestamp.

- **`are_friends_at(user_id1: str, user_id2: str, timestamp: int) -> bool`**  
  Returns whether the two users were friends at the specified timestamp.

- **`get_friends_at(user_id: str, timestamp: int) -> list[str]`**  
  Returns the list of friends at the specified timestamp, sorted lexicographically.

- **`get_mutual_friends_at(user_id1: str, user_id2: str, timestamp: int) -> list[str]`**  
  Returns mutual friends at the specified timestamp.

- **`get_friendship_duration(user_id1: str, user_id2: str, start_time: int, end_time: int) -> int`**  
  Returns the total time units the two users were friends during the interval `[start_time, end_time)`. Accounts for multiple add/remove cycles.

---

## Level 4: Posts & Social Features

Add posting functionality with visibility rules and friend recommendations.

### Important Notes:
- Posts are visible only to the author's friends at the time of viewing.
- Friend recommendations use "friends of friends" logic.
- Blocked users cannot see each other's posts or be recommended as friends.

### Methods to Implement:

- **`create_post(user_id: str, post_id: str, content: str, timestamp: int) -> bool`**  
  Creates a post by the user at the given timestamp. Returns `True` if successful, `False` if user doesn't exist or post_id already exists.

- **`get_post(post_id: str, viewer_id: str, timestamp: int) -> str | None`**  
  Returns the post content if the viewer can see it at the given timestamp. A user can see a post if:
  - They are the author, OR
  - They are friends with the author at the viewing timestamp
  
  Returns `None` if post doesn't exist, viewer doesn't exist, or viewer cannot see the post.

- **`get_feed(user_id: str, timestamp: int) -> list[str]`**  
  Returns a list of post_ids visible to the user at the timestamp, sorted by post creation time (most recent first). Includes the user's own posts and friends' posts.

- **`block_user(blocker_id: str, blocked_id: str, timestamp: int) -> bool`**  
  User `blocker_id` blocks `blocked_id` starting at timestamp. Blocking is NOT bidirectional — A blocking B doesn't mean B blocks A. Returns `True` if successful, `False` if either user doesn't exist or already blocked.

- **`get_friend_recommendations(user_id: str, timestamp: int) -> list[str]`**  
  Returns recommended friends (friends of friends who are not already friends and not blocked in either direction), sorted by number of mutual friends (descending), then by user_id (ascending) for ties. Limit to top 5.

---

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests for a specific level
pytest tests/ -v -k "level1"
pytest tests/ -v -k "level2"
pytest tests/ -v -k "level3"
pytest tests/ -v -k "level4"
```

## Tips

1. **Bidirectional friendships:** Remember to maintain both directions when adding/removing.
2. **Graph thinking:** Friends-of-friends is essentially a 2-hop BFS.
3. **Time complexity:** Consider using sets for O(1) friendship lookups.
4. **Blocking asymmetry:** A blocks B ≠ B blocks A. Handle this carefully.

Good luck! 🚀
