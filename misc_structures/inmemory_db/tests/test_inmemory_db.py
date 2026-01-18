import pytest
from inmemory_db.inmemory_db import InMemoryDB


class TestInMemoryDB:
    """Test suite for InMemoryDB class"""
    
    def setup_method(self):
        """Create a fresh database instance before each test"""
        self.db = InMemoryDB()
    
    # Add your tests here
    def test_null_key_getter(self):
        res = self.db.get("hey","bye")
        assert res is None

    def test_set_get(self):
        self.db.set("person","colour","black")
        colour = self.db.get("person","colour")
        assert colour == "black"

    def test_set_override(self):
        self.db.set("person","colour","black")
        self.db.set("person","colour","white")
        colour = self.db.get("person","colour")
        assert colour == "white"

    def test_set_delete(self):
        self.db.set("person","colour","black")
        del_res = self.db.delete("person","name")
        assert del_res is False
        del_res = self.db.delete("person","colour")
        assert del_res is True
        colour = self.db.get("person","colour")
        assert colour is None

    def test_scan(self):
        self.db.set("person","name","guillermo")
        self.db.set("person","surname","santamaria")
        scan_res = self.db.scan("person")
        assert scan_res == ["name(guillermo)","surname(santamaria)"]

    def test_scan_rev(self):
        self.db.set("person","surname","santamaria")
        self.db.set("person","name","guillermo")
        self.db.set("person","colour","pink")
        scan_res = self.db.scan("person")
        assert scan_res == ["colour(pink)","name(guillermo)","surname(santamaria)"]

    def test_scan_filt(self):
        self.db.set("person","name","guillermo")
        self.db.set("person","surname","santamaria")
        scan_res = self.db.scan_by_prefix("person","name")
        assert scan_res == ["name(guillermo)"]

    def test_scan_filt_empty(self):
        self.db.set("person","name","guillermo")
        self.db.set("person","surname","santamaria")
        scan_res = self.db.scan_by_prefix("person","yey")
        assert scan_res == []


    def test_scan_filt_all(self):
        self.db.set("person","surname","santamaria")
        self.db.set("person","suriname","guillermo")
        self.db.set("person","colour","pink")
        scan_res = self.db.scan_by_prefix("person","sur")
        assert scan_res == ["suriname(guillermo)","surname(santamaria)"]

    def test_set_at_get_exists(self):
        self.db.set_at("person","name","guillermo",10)
        name = self.db.get_at("person","name",20)
        assert name == "guillermo"

    def test_set_at_ttl_get_exists(self):
        self.db.set_at_with_ttl("person","name","guillermo",10,20)
        name = self.db.get_at("person","name",20)
        assert name == "guillermo"

    def test_set_at_ttl_get_expired(self):
        self.db.set_at_with_ttl("person","name","guillermo",10,20)
        name = self.db.get_at("person","name",50)
        assert name is None

    def test_set_at_ttl_delete_not_expired(self):
        self.db.set_at_with_ttl("person","name","guillermo",10,20)
        deleted = self.db.delete_at("person","name",20)
        assert deleted is True

    def test_set_at_ttl_delete_expired(self):
        self.db.set_at_with_ttl("person","name","guillermo",10,20)
        deleted = self.db.delete_at("person","name",50)
        assert deleted is False