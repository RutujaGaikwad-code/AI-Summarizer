#!/usr/bin/env python3
"""
Test script for the authentication system
"""

import os
import sys
import json
from auth import (
    load_users, save_users, hash_password, verify_password,
    is_valid_email, is_valid_password, register_user, login_user
)

def test_password_hashing():
    """Test password hashing and verification"""
    print("Testing password hashing...")
    password = "TestPassword123"
    hashed = hash_password(password)
    
    assert hashed != password, "Password should be hashed"
    assert verify_password(password, hashed), "Password verification should work"
    assert not verify_password("WrongPassword", hashed), "Wrong password should fail"
    print("✅ Password hashing test passed")

def test_email_validation():
    """Test email validation"""
    print("Testing email validation...")
    
    valid_emails = [
        "test@example.com",
        "user.name@domain.co.uk",
        "user+tag@example.org"
    ]
    
    invalid_emails = [
        "invalid-email",
        "@example.com",
        "user@",
        "user@.com"
    ]
    
    for email in valid_emails:
        assert is_valid_email(email), f"Valid email {email} should pass"
    
    for email in invalid_emails:
        assert not is_valid_email(email), f"Invalid email {email} should fail"
    
    print("✅ Email validation test passed")

def test_password_validation():
    """Test password strength validation"""
    print("Testing password validation...")
    
    valid_passwords = [
        "TestPass123",
        "MySecurePassword1",
        "ComplexP@ssw0rd"
    ]
    
    invalid_passwords = [
        "short",  # Too short
        "nouppercase123",  # No uppercase
        "NOLOWERCASE123",  # No lowercase
        "NoNumbers",  # No numbers
    ]
    
    for password in valid_passwords:
        is_valid, message = is_valid_password(password)
        assert is_valid, f"Valid password {password} should pass: {message}"
    
    for password in invalid_passwords:
        is_valid, message = is_valid_password(password)
        assert not is_valid, f"Invalid password {password} should fail: {message}"
    
    print("✅ Password validation test passed")

def test_user_registration():
    """Test user registration"""
    print("Testing user registration...")
    
    # Clean up any existing test data
    if os.path.exists("users.json"):
        os.remove("users.json")
    
    # Test successful registration
    success, message = register_user("testuser", "test@example.com", "TestPass123")
    assert success, f"Registration should succeed: {message}"
    
    # Test duplicate username
    success, message = register_user("testuser", "another@example.com", "TestPass123")
    assert not success, "Duplicate username should fail"
    
    # Test duplicate email
    success, message = register_user("anotheruser", "test@example.com", "TestPass123")
    assert not success, "Duplicate email should fail"
    
    # Test invalid email
    success, message = register_user("newuser", "invalid-email", "TestPass123")
    assert not success, "Invalid email should fail"
    
    # Test weak password
    success, message = register_user("newuser", "valid@example.com", "weak")
    assert not success, "Weak password should fail"
    
    print("✅ User registration test passed")

def test_user_login():
    """Test user login"""
    print("Testing user login...")
    
    # Test successful login
    success, message = login_user("testuser", "TestPass123")
    assert success, f"Login should succeed: {message}"
    
    # Test wrong password
    success, message = login_user("testuser", "WrongPassword")
    assert not success, "Wrong password should fail"
    
    # Test non-existent user
    success, message = login_user("nonexistent", "TestPass123")
    assert not success, "Non-existent user should fail"
    
    print("✅ User login test passed")

def test_data_persistence():
    """Test that user data persists correctly"""
    print("Testing data persistence...")
    
    # Load users and verify test user exists
    users = load_users()
    assert "testuser" in users, "Test user should exist in saved data"
    assert users["testuser"]["email"] == "test@example.com", "Email should be saved correctly"
    
    print("✅ Data persistence test passed")

def cleanup():
    """Clean up test data"""
    print("Cleaning up test data...")
    if os.path.exists("users.json"):
        os.remove("users.json")
    print("✅ Cleanup completed")

def main():
    """Run all tests"""
    print("🧪 Running authentication system tests...\n")
    
    try:
        test_password_hashing()
        test_email_validation()
        test_password_validation()
        test_user_registration()
        test_user_login()
        test_data_persistence()
        
        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    
    finally:
        cleanup()

if __name__ == "__main__":
    main()
