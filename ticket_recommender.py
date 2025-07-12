from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class TicketRecommender:
    def __init__(
        self,
        data,
        text_column='Customer Remarks',
        context_columns=['Product_category'],
        output_columns=['Customer Remarks', 'Sub-category'],
        model_name='all-MiniLM-L6-v2'
    ):
        # Keep only rows with non-null customer remarks
        self.df = data.dropna(subset=[text_column])
        self.text_column = text_column
        self.context_columns = context_columns
        self.output_columns = output_columns

        # Load SBERT model
        self.model = SentenceTransformer(model_name)

        # Create enriched text by combining remarks + context columns
        self.df['combined_text'] = self.df.apply(
            lambda row: row[text_column] + ' ' + ' '.join(
                str(row[col]) for col in context_columns if pd.notna(row[col])
            ),
            axis=1
        )

        # Generate embeddings for all tickets
        self.embeddings = self.model.encode(
            self.df['combined_text'].tolist(),
            show_progress_bar=True
        )

    def recommend(self, query, context_data=None, top_n=5):
        # Enrich query with contextual values if provided
        if context_data:
            query += ' ' + ' '.join(
                str(context_data.get(col, '')) for col in self.context_columns
            )

        # Generate embedding for input query
        query_vec = self.model.encode([query])

        # Compute similarity scores
        similarities = cosine_similarity(query_vec, self.embeddings).flatten()
        top_indices = similarities.argsort()[-top_n:][::-1]

        # Return top N most similar rows
        return self.df.iloc[top_indices][self.output_columns]
