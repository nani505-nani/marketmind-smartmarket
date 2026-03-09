import React, { useState, useEffect } from 'react';

const MarketMindDashboard = () => {
  // State to hold our product data and search input
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(true);

  // Simulating an API call to your backend
  useEffect(() => {
    // Mock data representing what your AI backend would return
    const mockTrendingData = [
      { id: 1, name: 'Ergonomic Standing Desk', category: 'Office', trendScore: 95, status: 'Rising Fast' },
      { id: 2, name: 'Matcha Whisk Set', category: 'Kitchen', trendScore: 88, status: 'Steady Growth' },
      { id: 3, name: 'Weighted Sleep Mask', category: 'Health', trendScore: 72, status: 'Fading Fad' },
      { id: 4, name: 'Portable Solar Charger', category: 'Electronics', trendScore: 91, status: 'Rising Fast' },
    ];

    // Simulate network delay
    setTimeout(() => {
      setProducts(mockTrendingData);
      setIsLoading(false);
    }, 1000);
  }, []);

  // Filter products based on user search
  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      {/* Header Section */}
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">MarketMind Dashboard</h1>
        <p className="text-gray-600">Discover what your customers want before they do.</p>
      </header>

      {/* Search Bar */}
      <div className="mb-6">
        <input
          type="text"
          placeholder="Search for products or categories..."
          className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      {/* Data Display Section */}
      {isLoading ? (
        <p className="text-lg text-gray-500 font-semibold">Analyzing market trends...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredProducts.length === 0 ? (
  <p className="text-gray-500">No products found matching your search.</p>
) : (
  // existing grid content
)}
            <div key={product.id} className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow">
              <div className="flex justify-between items-start mb-4">
                <h2 className="text-xl font-semibold text-gray-800">{product.name}</h2>
                <span className="bg-blue-100 text-blue-800 text-xs font-bold px-2 py-1 rounded">
                  {product.category}
                </span>
              </div>
              
              <div className="mb-2">
                <span className="text-sm text-gray-500">Trend Score:</span>
                <div className="w-full bg-gray-200 rounded-full h-2.5 mt-1">
                  <div 
                    className="bg-green-500 h-2.5 rounded-full" 
                    style={{ width: `${product.trendScore}%` }}
                  ></div>
                </div>
              </div>
              
              <p className="text-sm font-medium mt-4">
                const getStatusColor = (status) => {
  switch(status) {
    case 'Rising Fast': return 'text-green-600';
    case 'Steady Growth': return 'text-blue-600';
    case 'Fading Fad': return 'text-orange-500';
    default: return 'text-gray-600';
  }
};
                  {product.status}
                </span>
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};


export default MarketMindDashboard;
