// Production-ready configuration
export const getBaseUrl = () => {
  // In production, use environment variable or detect from request
  if (process.env.NEXTAUTH_URL) {
    return process.env.NEXTAUTH_URL
  }
  
  // Development fallbacks
  if (process.env.NODE_ENV === 'development') {
    return 'http://localhost:3001'
  }
  
  // Production fallback - should be set via environment
  return 'https://your-domain.com'
}

export const getAuthConfig = () => {
  const baseUrl = getBaseUrl()
  
  return {
    baseUrl,
    secret: process.env.NEXTAUTH_SECRET || 'fallback-secret-key',
    debug: process.env.NODE_ENV === 'development',
    secureCookies: process.env.NODE_ENV === 'production'
  }
}

// Database configuration
export const getDatabaseConfig = () => {
  return {
    url: process.env.DATABASE_URL,
    maxConnections: parseInt(process.env.DATABASE_MAX_CONNECTIONS || '10'),
    timeout: parseInt(process.env.DATABASE_TIMEOUT || '30000')
  }
}

// API configuration
export const getApiConfig = () => {
  return {
    rateLimit: {
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100 // limit each IP to 100 requests per windowMs
    },
    cors: {
      origin: process.env.NODE_ENV === 'production' 
        ? process.env.ALLOWED_ORIGINS?.split(',') || []
        : ['http://localhost:3001', 'http://127.0.0.1:3001', 'http://172.20.10.3:3001'],
      credentials: true
    }
  }
}
