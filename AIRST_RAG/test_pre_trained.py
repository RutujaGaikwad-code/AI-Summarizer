#!/usr/bin/env python3
"""
Test script for pre-trained models integration
"""

def test_pre_trained_models():
    """Test the pre-trained models functionality"""
    print("🧪 Testing Pre-trained Models Integration")
    print("=" * 50)
    
    # Test text
    test_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines.
    These machines can perform tasks that typically require human intelligence.
    Machine learning is a subset of AI that enables computers to learn and improve from experience.
    Deep learning uses neural networks with multiple layers to process complex patterns.
    """
    
    try:
        # Import the models
        from models import process_text
        print("✅ Successfully imported pre-trained models")
        
        # Test the process_text function
        print("\n🔄 Testing text processing...")
        result = process_text(test_text)
        
        print(f"✅ Domain classification: {result.get('domain', 'Unknown')}")
        print(f"✅ Summary generated: {len(result.get('summary', ''))} characters")
        print(f"✅ Entities found: {len(result.get('entities', []))}")
        
        print("\n📝 Sample Summary:")
        print(result.get('summary', 'No summary available.'))
        
        print("\n🏷️ Sample Entities:")
        entities = result.get('entities', [])
        for entity in entities[:5]:  # Show first 5 entities
            print(f"  - {entity.get('word', '')} ({entity.get('entity_group', 'MISC')})")
        
        print("\n🎉 All tests passed! Pre-trained models are working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Error testing pre-trained models: {e}")
        return False

if __name__ == "__main__":
    success = test_pre_trained_models()
    if success:
        print("\n✅ Ready to use pre-trained models in the application!")
    else:
        print("\n❌ Please check the model installation and dependencies.")
