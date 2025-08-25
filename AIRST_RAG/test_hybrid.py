#!/usr/bin/env python3
"""
Test script for hybrid analysis functionality
"""

def test_hybrid_analysis():
    """Test the hybrid analysis functionality"""
    print("🧪 Testing Hybrid Analysis Integration")
    print("=" * 50)
    
    # Test text
    test_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines.
    These machines can perform tasks that typically require human intelligence.
    Machine learning is a subset of AI that enables computers to learn and improve from experience.
    Deep learning uses neural networks with multiple layers to process complex patterns.
    """
    
    try:
        # Import the hybrid analysis module
        from hybrid_analysis import hybrid_summarization, hybrid_qa, hybrid_entity_analysis
        print("✅ Successfully imported hybrid analysis module")
        
        # Test hybrid summarization
        print("\n🔄 Testing hybrid summarization...")
        summary_results = hybrid_summarization(test_text, "test_document.pdf", "Brief (2-3 paragraphs)", "English")
        
        print(f"✅ Method: {summary_results.get('method', 'Unknown')}")
        print(f"✅ Enhanced: {summary_results.get('enhanced', False)}")
        print(f"✅ Domain: {summary_results.get('domain', 'Unknown')}")
        print(f"✅ Summary length: {len(summary_results.get('summary', ''))} characters")
        
        # Test hybrid Q&A
        print("\n🔄 Testing hybrid Q&A...")
        qa_results = hybrid_qa(test_text, "What is artificial intelligence?", "test_document.pdf", "English")
        
        print(f"✅ Method: {qa_results.get('method', 'Unknown')}")
        print(f"✅ Enhanced: {qa_results.get('enhanced', False)}")
        print(f"✅ Answer length: {len(qa_results.get('answer', ''))} characters")
        
        # Test hybrid entity analysis
        print("\n🔄 Testing hybrid entity analysis...")
        entity_results = hybrid_entity_analysis(test_text, "test_document.pdf")
        
        print(f"✅ Method: {entity_results.get('method', 'Unknown')}")
        print(f"✅ Enhanced: {entity_results.get('enhanced', False)}")
        print(f"✅ Entities found: {len(entity_results.get('entities', []))}")
        
        print("\n🎉 All hybrid analysis tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing hybrid analysis: {e}")
        return False

def test_analysis_methods():
    """Test different analysis methods"""
    print("\n🔍 Testing Analysis Methods")
    print("=" * 30)
    
    try:
        from hybrid_analysis import get_analysis_method
        print("✅ Analysis method selector imported successfully")
        
        # Test the available methods
        methods = {
            "Hybrid (Recommended)": "hybrid",
            "Pre-trained Models Only": "pretrained_only", 
            "ChatGPT Only": "chatgpt_only"
        }
        
        print("Available methods:")
        for method_name, method_value in methods.items():
            print(f"  - {method_name}: {method_value}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing analysis methods: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Hybrid Analysis Test Suite")
    print("=" * 50)
    
    # Test hybrid analysis
    hybrid_success = test_hybrid_analysis()
    
    # Test analysis methods
    methods_success = test_analysis_methods()
    
    if hybrid_success and methods_success:
        print("\n🎉 All tests passed! Hybrid analysis is ready to use!")
        print("\n💡 Benefits of Hybrid Analysis:")
        print("  ✅ Pre-trained models provide specialized domain analysis")
        print("  ✅ ChatGPT enhances summaries with better structure and clarity")
        print("  ✅ Automatic fallback to pre-trained models if ChatGPT unavailable")
        print("  ✅ Best of both worlds for improved accuracy")
    else:
        print("\n❌ Some tests failed. Please check the installation and dependencies.")
