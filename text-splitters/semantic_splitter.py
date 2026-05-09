"""Semantic-aware text splitter example.

This splitter divides text based on semantic meaning using embeddings.
It creates chunks that preserve semantic coherence.
Useful for: long-form content, topic-based splitting, preserving context.

Note: Requires OpenAI API key for embeddings. Set OPENAI_API_KEY environment variable.
"""

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker


text = """Machine learning is a subset of artificial intelligence that enables systems
to learn and improve from experience without being explicitly programmed. It focuses
on developing algorithms that can analyze data, identify patterns, and make predictions.
Machine learning models are trained on large datasets and can be applied to various tasks
such as image recognition, natural language processing, and recommendation systems.
The performance of these models depends heavily on data quality, feature engineering,
and hyperparameter tuning.

The Great Wall of China is one of the most impressive architectural wonders in human history.
Constructed over many centuries, it stretches over 13,000 miles across northern China.
The wall was built to protect against invasions from nomadic groups and to regulate trade
along the Silk Road. Today, it stands as a symbol of Chinese civilization and attracts
millions of tourists from around the world each year. The wall features watchtowers,
garrison stations, and steep mountain paths that showcase ancient engineering excellence.

Software engineering is a discipline that applies systematic, disciplined, and quantifiable
approaches to the development, operation, and maintenance of software. It combines principles
from computer science, project management, and empirical software engineering. Modern software
engineering involves practices such as version control, continuous integration, automated testing,
and agile methodologies to ensure high-quality, maintainable code.
"""

print("=== Semantic Text Chunker ===")
print("Note: This example requires OPENAI_API_KEY environment variable.\n")

try:
    # Initialize embeddings (requires OpenAI API key)
    embeddings = OpenAIEmbeddings()

    # breakpoint_threshold_type: Strategy for determining chunk boundaries
    #   - "standard_deviation": Uses statistical distance metric
    #   - "percentile": Uses percentile-based threshold
    # breakpoint_threshold_amount: Sensitivity level (higher = fewer, larger chunks)
    splitter = SemanticChunker(
        embeddings,
        breakpoint_threshold_type="standard_deviation",
        breakpoint_threshold_amount=1.0
    )

    chunks = splitter.split_text(text)

    print(f"Total semantic chunks: {len(chunks)}\n")
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i} ({len(chunk)} chars):")
        print(f"{chunk[:150]}...\n")
        print("-" * 50)

except Exception as e:
    print(f"Error: {e}")
    print(
        "Make sure OPENAI_API_KEY environment variable is set with a valid OpenAI API key."
    )
