"""
Unit & Integration Tests for Task Manager REST API
Author: Vaddi Ranga Koushik
"""

import unittest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../backend"))

from app import app, init_db, DB_PATH


class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client and initialize a fresh test database."""
        app.config["TESTING"] = True
        # Use an in-memory DB for tests
        import app as app_module
        app_module.DB_PATH = ":memory:"
        self.client = app.test_client()
        with app.app_context():
            init_db()

    def _create_task(self, title="Test Task", description="Test Desc", status="pending"):
        return self.client.post(
            "/api/tasks",
            data=json.dumps({"title": title, "description": description, "status": status}),
            content_type="application/json"
        )

    # ── CREATE ─────────────────────────────────────────────
    def test_create_task_success(self):
        """Should create a task and return 201."""
        res = self._create_task("Buy groceries", "Milk, Bread", "pending")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertEqual(data["title"], "Buy groceries")
        self.assertEqual(data["status"], "pending")

    def test_create_task_missing_title(self):
        """Should return 400 if title is missing."""
        res = self.client.post(
            "/api/tasks",
            data=json.dumps({"description": "No title"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 400)

    # ── READ ───────────────────────────────────────────────
    def test_get_all_tasks_empty(self):
        """Should return empty list when no tasks exist."""
        res = self.client.get("/api/tasks")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data), [])

    def test_get_all_tasks(self):
        """Should return all created tasks."""
        self._create_task("Task 1")
        self._create_task("Task 2")
        res = self.client.get("/api/tasks")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(json.loads(res.data)), 2)

    def test_get_single_task(self):
        """Should return a specific task by ID."""
        self._create_task("Specific Task")
        res = self.client.get("/api/tasks/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data)["title"], "Specific Task")

    def test_get_nonexistent_task(self):
        """Should return 404 for a task that doesn't exist."""
        res = self.client.get("/api/tasks/999")
        self.assertEqual(res.status_code, 404)

    # ── UPDATE ─────────────────────────────────────────────
    def test_update_task(self):
        """Should update task fields and return updated data."""
        self._create_task("Old Title")
        res = self.client.put(
            "/api/tasks/1",
            data=json.dumps({"title": "New Title", "status": "completed"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["title"], "New Title")
        self.assertEqual(data["status"], "completed")

    def test_update_nonexistent_task(self):
        """Should return 404 when updating a task that doesn't exist."""
        res = self.client.put(
            "/api/tasks/999",
            data=json.dumps({"title": "Ghost"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 404)

    # ── DELETE ─────────────────────────────────────────────
    def test_delete_task(self):
        """Should delete a task and return success message."""
        self._create_task("To Delete")
        res = self.client.delete("/api/tasks/1")
        self.assertEqual(res.status_code, 200)
        # Verify it's gone
        res2 = self.client.get("/api/tasks/1")
        self.assertEqual(res2.status_code, 404)

    def test_delete_nonexistent_task(self):
        """Should return 404 when deleting a task that doesn't exist."""
        res = self.client.delete("/api/tasks/999")
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
