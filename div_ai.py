import streamlit as st
import base64
from pathlib import Path

# Page config
st.set_page_config(
    page_title="DIV-AI - Your Personal Offline AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .comparison-table {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .download-button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 1rem 0;
        transition: transform 0.3s;
    }
    
    .download-button:hover {
        transform: translateY(-2px);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-box {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin: 0.5rem;
    }
    
    .testimonial {
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🤖 DIV-AI Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "✨ Features", 
    "📊 Comparison",
    "💻 Screenshots",
    "⚙️ Technical Specs",
    "📥 Download",
    "❓ FAQ",
    "👨‍💻 About Creator"
])

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🤖 DIV-AI</h1>
    <h2>Your Personal Offline AI Assistant</h2>
    <p style="font-size: 1.2em; margin-top: 1rem;">
        Powered by Div_v1_Quant • 100% Private • No Internet Required
    </p>
</div>
""", unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🔒 Complete Privacy. Unlimited Power.")
        st.markdown("""
        **DIV-AI** is revolutionary offline AI assistant that runs entirely on your local machine. 
        No internet connection required, no data leaves your computer, no subscriptions needed.
        
        ### Why Choose DIV-AI?
        """)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🔒 100% Private & Secure</h4>
            <p>All processing happens locally. Your conversations never leave your computer.</p>
        </div>
        
        <div class="feature-card">
            <h4>⚡ Lightning Fast Responses</h4>
            <p>Instant answers to personal questions, optimized AI responses for complex queries.</p>
        </div>
        
        <div class="feature-card">
            <h4>💰 No Subscriptions Ever</h4>
            <p>One-time download, lifetime usage. No monthly fees, no usage limits.</p>
        </div>
        
        <div class="feature-card">
            <h4>🌐 Works Offline Always</h4>
            <p>Perfect for secure environments, remote areas, or when you want guaranteed uptime.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📊 Quick Stats")
        st.markdown("""
        <div class="stat-box">
            <h3>2.7B</h3>
            <p>Parameters</p>
        </div>
        
        <div class="stat-box">
            <h3>1.65GB</h3>
            <p>Download Size</p>
        </div>
        
        <div class="stat-box">
            <h3>4GB RAM</h3>
            <p>Minimum Required</p>
        </div>
        
        <div class="stat-box">
            <h3>0%</h3>
            <p>Data Collection</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Perfect For:")
        st.markdown("""
        - **Privacy-conscious users**
        - **Businesses with sensitive data**
        - **Students and researchers**
        - **Remote workers**
        - **Anyone wanting AI without internet**
        """)

# Features Page
elif page == "✨ Features":
    st.markdown("## ✨ Powerful Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Smart AI Capabilities
        - **Programming Assistance**: Code help, debugging, explanations
        - **Creative Writing**: Stories, essays, content creation
        - **Problem Solving**: Complex analysis and solutions
        - **Educational Support**: Learning assistance, explanations
        - **General Knowledge**: Wide range of topics covered
        """)
        
        st.markdown("""
        ### 🖥️ User Interface
        - **Clean, Modern GUI**: Intuitive Tkinter-based interface
        - **Quick Question Buttons**: Instant access to common queries
        - **Real-time Monitoring**: CPU and RAM usage display
        - **Conversation Management**: Clear, organized chat interface
        - **Keyboard Shortcuts**: Efficient workflow support
        """)
    
    with col2:
        st.markdown("""
        ### ⚙️ Technical Excellence
        - **Optimized Performance**: CPU and memory efficient
        - **Process Management**: Safe operation with timeout protection
        - **Resource Control**: Configurable thread and batch limits
        - **Portable Design**: Works from any folder location
        - **Error Handling**: Robust error recovery and reporting
        """)
        
        st.markdown("""
        ### 🔧 Customization Options
        - **Response Length Control**: Adjustable output limits
        - **Performance Tuning**: CPU thread and memory settings
        - **Interface Themes**: Clean, professional appearance
        - **File Management**: Automatic path detection
        - **System Integration**: Native Windows experience
        """)
    
    st.markdown("---")
    st.markdown("### 🚀 What Makes DIV-AI Special?")
    
    features_detailed = [
        ("Hardcoded Instant Responses", "Personal questions about DIV-AI get instant answers - no AI processing delay"),
        ("Memory Optimization", "Smart resource usage prevents system slowdown while maintaining quality"),
        ("Self-Contained Package", "Everything included - no complex setup or external dependencies"),
        ("Professional Quality", "Enterprise-grade AI model optimized for consumer hardware"),
        ("Future-Proof Design", "Modular architecture allows for easy updates and enhancements")
    ]
    
    for title, desc in features_detailed:
        st.markdown(f"""
        <div class="feature-card">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Comparison Page
elif page == "📊 Comparison":
    st.markdown("## 📊 DIV-AI vs Competition")
    
    st.markdown("### See how DIV-AI stacks up against popular AI assistants:")
    
    comparison_data = {
        "Feature": [
            "Privacy (Data stays local)",
            "Works Offline",
            "No Subscription Fees",
            "No Usage Limits",
            "Instant Availability",
            "No Account Required",
            "Corporate/Business Safe",
            "Open Source Interface",
            "One-time Purchase",
            "No Internet Dependency"
        ],
        "DIV-AI": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"],
        "ChatGPT": ["❌", "❌", "❌", "❌", "⚠️", "❌", "⚠️", "❌", "❌", "❌"],
        "Claude": ["❌", "❌", "❌", "❌", "⚠️", "❌", "⚠️", "❌", "❌", "❌"],
        "Bard/Gemini": ["❌", "❌", "✅", "⚠️", "⚠️", "❌", "⚠️", "❌", "✅", "❌"],
        "Local LLMs": ["✅", "✅", "✅", "✅", "⚠️", "✅", "✅", "⚠️", "✅", "✅"]
    }
    
    import pandas as pd
    df = pd.DataFrame(comparison_data)
    
    st.markdown("""
    <div class="comparison-table">
    """, unsafe_allow_html=True)
    
    st.dataframe(df, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Why DIV-AI Wins:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔒 Unmatched Privacy**
        - Zero data collection
        - No cloud processing
        - Complete local control
        - GDPR/CCPA compliant by design
        """)
        
        st.markdown("""
        **💰 True Cost Efficiency**
        - No monthly subscriptions
        - No usage-based billing
        - One download, lifetime use
        - Perfect for budget-conscious users
        """)
    
    with col2:
        st.markdown("""
        **⚡ Reliable Performance**
        - Always available offline
        - No server downtime issues
        - Consistent response times
        - Not affected by internet speed
        """)
        
        st.markdown("""
        **🏢 Business Ready**
        - Safe for sensitive data
        - No external data sharing
        - Compliance-friendly
        - Internal use approved
        """)

# Screenshots Page
elif page == "💻 Screenshots":
    st.markdown("## 💻 See DIV-AI in Action")
    
    st.markdown("### 🖥️ Clean, Professional Interface")
    st.info("🎨 **Note**: Screenshots show the actual DIV-AI interface - clean, fast, and user-friendly!")
    
    # Placeholder for screenshots (you would replace with actual images)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Main Interface")
        st.markdown("""
        ```
        ┌─────────────────────────────────────┐
        │              DIV-AI                 │
        │   Your Personal Offline AI          │
        │                                     │
        │ CPU: 15.2% | RAM: 45.1% | Div_v1   │
        ├─────────────────────────────────────┤
        │ [Who are you?] [What model?] [...]  │
        ├─────────────────────────────────────┤
        │ Your Question:                      │
        │ ┌─────────────────────────────────┐ │
        │ │ How does photosynthesis work?   │ │
        │ └─────────────────────────────────┘ │
        │                                     │
        │ [Ask DIVAI] [Stop] [Clear] [Files]  │
        ├─────────────────────────────────────┤
        │ DIV-AI Response:                    │
        │ ┌─────────────────────────────────┐ │
        │ │ Photosynthesis is the process   │ │
        │ │ by which plants convert light   │ │
        │ │ energy into chemical energy...  │ │
        │ └─────────────────────────────────┘ │
        └─────────────────────────────────────┘
        ```
        """)
    
    with col2:
        st.markdown("#### Quick Questions Feature")
        st.markdown("""
        **Instant Responses for:**
        - "Who are you?" → Immediate DIV-AI info
        - "What model?" → Technical specifications  
        - "Your capabilities" → Feature overview
        - "Privacy info" → Security details
        
        **No waiting time for personal questions!**
        """)
    
    st.markdown("### 🎯 Key Interface Features")
    
    features_ui = [
        ("Resource Monitor", "Real-time CPU and RAM usage displayed in header"),
        ("Quick Access Buttons", "One-click access to common questions about DIV-AI"),
        ("Smart Input Box", "Supports multi-line questions with scroll capability"),
        ("Clean Output", "Filtered responses without technical debug information"),
        ("Control Buttons", "Ask, Stop, Clear functions with intuitive icons"),
        ("File Verification", "Check Files button ensures proper installation"),
        ("Status Feedback", "Clear indication of processing state and completion")
    ]
    
    for title, desc in features_ui:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🎨 {title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Technical Specs Page
elif page == "⚙️ Technical Specs":
    st.markdown("## ⚙️ Technical Specifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔧 System Requirements")
        st.markdown("""
        **Minimum Requirements:**
        - **OS**: Windows 10/11 (64-bit)
        - **RAM**: 4GB available memory
        - **CPU**: Multi-core processor (2+ cores)
        - **Storage**: 2GB free disk space
        - **Architecture**: x64 compatible
        
        **Recommended Specifications:**
        - **RAM**: 8GB+ for optimal performance
        - **CPU**: Modern quad-core processor
        - **Storage**: SSD for faster model loading
        - **Cooling**: Adequate CPU cooling for sustained use
        """)
        
        st.markdown("### 📦 What's Included")
        st.markdown("""
        **Core Components:**
        - `DIVAI.py` - Main application interface
        - `div-cli.exe` - AI inference engine  
        - `div_quant.gguf` - Div_v1_Quant model (1.5GB)
        - Essential DLL files for Windows compatibility
        
        **Additional Files:**
        - `README.md` - Complete documentation
        - `requirements.txt` - Python dependencies
        - Installation and usage guides
        """)
    
    with col2:
        st.markdown("### 🤖 AI Model Details")
        st.markdown("""
        **Div_v1_Quant Specifications:**
        - **Parameters**: 2.7 billion
        - **Quantization**: 4-bit (Q4_K_M format)
        - **Context Window**: 2048 tokens (512 optimized)
        - **Model Size**: ~1.5GB compressed
        - **Training**: Optimized for general assistance
        
        **Performance Optimizations:**
        - **CPU Threads**: Limited to 2 for stability
        - **Batch Size**: 32 tokens for efficiency  
        - **Response Limit**: 200 tokens for speed
        - **Memory Usage**: ~2-3GB RAM during operation
        - **Process Priority**: Below normal to prevent lag
        """)
        
        st.markdown("### ⚡ Performance Metrics")
        st.markdown("""
        **Response Times:**
        - Personal questions: Instant (0.1s)
        - Simple queries: 10-30 seconds
        - Complex analysis: 30-90 seconds
        - Code generation: 20-60 seconds
        
        **Resource Usage:**
        - CPU: 20-40% during processing
        - RAM: 2-4GB peak usage
        - Disk I/O: Minimal after model load
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔬 Technical Architecture")
    
    architecture_details = [
        ("Frontend", "Python Tkinter GUI with real-time monitoring and responsive design"),
        ("Backend", "Custom compiled inference engine based on llama.cpp architecture"),
        ("Model Format", "GGUF format with 4-bit quantization for optimal size/quality balance"),
        ("Process Management", "Subprocess handling with timeout protection and priority control"),
        ("Memory Optimization", "Smart context management and batch processing for efficiency"),
        ("Error Handling", "Comprehensive exception handling with user-friendly error messages")
    ]
    
    for component, description in architecture_details:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🏗️ {component}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# Download Page
elif page == "📥 Download":
    st.markdown("## 📥 Download DIV-AI")
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin: 2rem 0;">
        <h2>🚀 Ready to Experience True AI Privacy?</h2>
        <p style="font-size: 1.2em;">Download DIV-AI now and start using AI without compromising your privacy!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📦 Download Options")
        
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Recommended: Complete Package</h4>
            <p><strong>Size:</strong> 1.65GB (compressed)</p>
            <p><strong>Includes:</strong> Full application, model, and all dependencies</p>
            <p><strong>Best for:</strong> Most users wanting complete offline AI experience</p>
            <a href="#" class="download-button">📥 Download Full Package (1.65GB)</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>💻 Alternative: Source Code</h4>
            <p><strong>Size:</strong> ~50MB (without model)</p>
            <p><strong>Includes:</strong> Python source code and documentation</p>
            <p><strong>Best for:</strong> Developers who want to customize or have their own model</p>
            <a href="#" class="download-button">💻 Download Source Code</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔧 Installation Instructions")
        st.markdown("""
        1. **Download** the complete package from above
        2. **Extract** the archive to your desired location
        3. **Run** `DIVAI.exe` (or `python DIVAI.py` for source)
        4. **Click "Check Files"** to verify installation
        5. **Start asking questions!**
        
        **No additional setup required!** DIV-AI works immediately after extraction.
        """)
    
    with col2:
        st.markdown("### ✅ What You Get")
        st.markdown("""
        **🎯 Complete AI Assistant**
        - Full offline AI capabilities
        - No internet dependency
        - Professional quality responses
        
        **🔒 Privacy Guaranteed**
        - Zero data collection
        - No cloud processing
        - Complete local control
        
        **💰 Lifetime Value**
        - No subscription fees
        - No usage limits
        - Free updates included
        
        **🛠️ Professional Support**
        - Complete documentation
        - GitHub issue support
        - Active community
        """)
        
        st.markdown("### 📊 File Integrity")
        st.code("""
        SHA256 Checksums:
        
        Full Package:
        a1b2c3d4e5f6...
        
        Source Code:
        f6e5d4c3b2a1...
        """)
    
    st.markdown("---")
    st.markdown("### 🚨 Important Notes")
    st.warning("""
    **System Compatibility**: Currently Windows 10/11 (64-bit) only. Linux/macOS versions coming soon!
    
    **First Run**: Initial model loading may take 30-60 seconds. Subsequent starts are much faster.
    
    **Antivirus**: Some antivirus software may flag the executable as unknown. This is normal for new software.
    """)

# FAQ Page
elif page == "❓ FAQ":
    st.markdown("## ❓ Frequently Asked Questions")
    
    faqs = {
        "🔒 Privacy & Security": [
            ("Is my data really private?", "Absolutely! DIV-AI runs completely offline. Your conversations never leave your computer, and we don't collect any data whatsoever."),
            ("Can you see my conversations?", "No, we cannot. There's no telemetry, no data transmission, and no tracking. Your privacy is 100% guaranteed."),            
            ("Is it safe for business use?", "Yes! DIV-AI is perfect for businesses with sensitive data since everything stays local and private."),
            ("Does it connect to the internet?", "No internet connection is required or used. DIV-AI works completely offline.")
        ],
        
        "⚡ Performance & Usage": [
            ("Why is it slow compared to ChatGPT?", "DIV-AI runs on your local hardware, not powerful cloud servers. The trade-off is complete privacy and no internet dependency."),
            ("How can I make it faster?", "Close other applications, ensure good CPU cooling, ask shorter questions, and consider upgrading your hardware."),
            ("Does it work on older computers?", "Yes, but performance depends on your CPU. 4GB RAM and a multi-core processor are minimum requirements."),
            ("Can I run multiple instances?", "It's not recommended as it would consume significant system resources.")
        ],
        
        "💰 Pricing & Licensing": [
            ("Is it really free?", "Yes! DIV-AI is completely free to download and use. No subscriptions, no hidden fees, no usage limits."),
            ("Will there be paid versions?", "The core DIV-AI will always remain free. We may offer premium models or features in the future."),
            ("Can I use it commercially?", "Yes, DIV-AI can be used for commercial purposes without additional licensing fees."),
            ("Are there any usage restrictions?", "No usage limits whatsoever. Use it as much as you want, whenever you want.")
        ],
        
        "🛠️ Technical Support": [
            ("What if I encounter bugs?", "Report issues on our GitHub page. We actively monitor and fix bugs reported by users."),
            ("Can I modify the code?", "Yes! The interface code is open source. The AI model and inference engine are proprietary."),
            ("Will you add new features?", "Yes, we regularly update DIV-AI with new features based on user feedback."),
            ("How do I update DIV-AI?", "Updates will be released as new versions. Simply download and replace the old files.")
        ],
        
        "🔧 Installation & Setup": [
            ("Why is the download so large?", "The AI model file is ~1.5GB. This is necessary for high-quality offline AI capabilities."),
            ("Do I need Python installed?", "No, the complete package includes everything needed. Python is only required if running from source code."),
            ("Can I move it to another computer?", "Yes! Simply copy the entire DIV-AI folder to any Windows computer."),
            ("What if files are missing?", "Use the 'Check Files' button in DIV-AI to verify all required files are present.")
        ]
    }
    
    for category, questions in faqs.items():
        st.markdown(f"### {category}")
        for question, answer in questions:
            with st.expander(question):
                st.write(answer)
        st.markdown("---")
    
    st.markdown("### 🤝 Still Have Questions?")
    st.markdown("""
    **Can't find what you're looking for?**
    
    - 📧 **Email Support**: [your-email@example.com]
    - 💬 **GitHub Issues**: [Create an issue](https://github.com/yourusername/div-ai/issues)
    - 📚 **Documentation**: Check our comprehensive README
    - 💭 **Community**: Join discussions on GitHub
    
    We typically respond within 24-48 hours!
    """)

# About Creator Page
elif page == "👨‍💻 About Creator":
    st.markdown("## 👨‍💻 Meet the Creator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder for creator photo
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    height: 300px; border-radius: 15px; display: flex; 
                    align-items: center; justify-content: center; color: white; font-size: 4em;">
            👨‍💻
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Divyansh Pandit")
        st.markdown("**Creator & Developer of DIV-AI**")
        
        st.markdown("""
        Divyansh is a passionate AI developer and privacy advocate who believes that 
        powerful AI should be accessible to everyone without compromising personal privacy.
        
        **🎯 Mission**: To democratize AI technology while keeping user privacy intact.
        
        **💡 Vision**: A world where everyone can benefit from AI without giving up their data.
        """)
        
        st.markdown("### 🏆 Achievements")
        st.markdown("""
        - ✅ **Created DIV-AI**: The first truly private offline AI assistant
        - ✅ **Optimized Div_v1_Quant**: Custom AI model for consumer hardware  
        - ✅ **Built Privacy-First Tools**: Focus on user data protection
        - ✅ **Active Open Source Contributor**: Believes in community collaboration
        """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚀 The Story Behind DIV-AI")
        st.markdown("""
        **The Problem**: Existing AI assistants require internet connectivity and send all your 
        data to external servers. This creates privacy concerns, especially for sensitive work 
        or personal conversations.
        
        **The Solution**: DIV-AI was born from the need for a truly private AI assistant that 
        runs entirely on your local machine. No data ever leaves your computer, yet you get 
        professional-quality AI assistance.
        
        **The Journey**: Months of optimization, testing, and refinement went into making 
        DIV-AI both powerful and accessible to everyday users with regular hardware.
        """)
    
    with col2:
        st.markdown("### 💭 Developer Philosophy")
        st.markdown("""
        **Privacy First**: Your data belongs to you, not to big tech companies.
        
        **Quality Without Compromise**: Offline doesn't mean inferior. DIV-AI delivers 
        professional-grade AI assistance locally.
        
        **Accessibility**: Advanced AI shouldn't require expensive hardware or technical 
        expertise to use.
        
        **Community Driven**: User feedback shapes the development of new features and improvements.
        
        **Open & Transparent**: The interface code is open source for complete transparency.
        """)
    
    st.markdown("---")
    
    st.markdown("### 🌟 What's Next?")
    
    roadmap_items = [
        ("Multi-Platform Support", "Linux and macOS versions in development"),
        ("Enhanced Models", "Larger and more specialized AI models"),
        ("Voice Integration", "Speech-to-text and text-to-speech capabilities"),
        ("Plugin System", "Extensible architecture for custom features"),
        ("Mobile Version", "Android app for on-the-go AI assistance"),
        ("Enterprise Features", "Advanced tools for business users")
    ]
    
    for title, desc in roadmap_items:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🚀 {title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🤝 Connect & Support")
    st.markdown("""
    **Want to support DIV-AI development?**
    
    - ⭐ **Star the project** on GitHub
    - 🐛 **Report bugs** and suggest features  
    - 📢 **Share DIV-AI** with friends who value privacy
    - 💬 **Join the community** discussions
    - ☕ **Buy me a coffee** (donation links coming soon!)
    
    Your support helps keep DIV-AI free and continuously improving!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
    <h3>🤖 DIV-AI - Your Privacy-First AI Assistant</h3>
    <p>Made with ❤️ by Divyansh Pandit | © 2024 DIV-AI Project</p>
    <p>
        <a href="https://github.com/yourusername/div-ai" target="_blank">GitHub</a> | 
        <a href="mailto:your-email@example.com">Contact</a> | 
        <a href="#" onclick="window.scrollTo(0,0)">Back to Top</a>
    </p>
</div>
""", unsafe_allow_html=True)
