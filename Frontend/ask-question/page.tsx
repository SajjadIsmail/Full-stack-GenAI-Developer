'use client';

import { useState } from 'react';

const AskQuestionPage = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  // Function to handle question submission
  const handleSubmit = async () => {
    if (!question.trim()) {
      alert('Please enter a valid question.');
      return;
    }

    setLoading(true);
    setResponse(''); // Clear previous response while loading

    try {
      const res = await fetch('http://localhost:8080/chatmodel', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }), // Send the question in the request body
      });

      if (!res.ok) {
        throw new Error('Failed to fetch the response from the server.');
      }

      const text = await res.text(); // Assume the backend returns plain text
      setResponse(text); // Update response state
    } catch (error) {
      console.error(error);
      setResponse('Error: Could not fetch a response. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br  to-blue-500 from-purple-500 via-pink-500  text-white">
      <div className="bg-white text-black p-8 rounded-xl shadow-md max-w-lg w-full">
        <h1 className="text-2xl font-bold text-center mb-4">🤖 Ask a Question</h1>
        <div className="mb-4">
          <textarea
            className="w-full p-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
            rows={4}
            placeholder="Type your question here..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          ></textarea>
        </div>
        <button
          onClick={handleSubmit}
          className={`w-full py-2 px-4 rounded-lg text-white font-semibold transition-all ${
            loading
              ? 'bg-gray-400 cursor-not-allowed'
              : 'bg-green-600 hover:bg-green-700'
          }`}
          disabled={loading}
        >
          {loading ? 'Fetching Response...' : 'Submit Question'}
        </button>
        {response && (
          <div className="mt-6 bg-gray-100 p-4 border border-gray-300 rounded-lg text-black">
            <h2 className="font-bold mb-2">Response:</h2>
            <p>{response}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default AskQuestionPage;
