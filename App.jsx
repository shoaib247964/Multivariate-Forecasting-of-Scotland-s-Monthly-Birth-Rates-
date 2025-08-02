import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { TrendingDown, TrendingUp, Users, Briefcase, BarChart3, Calendar, MapPin } from 'lucide-react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import analysisChart from './assets/economic_demographic_analysis.png'
import './App.css'

function App() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    setIsVisible(true)
  }, [])

  const stats = [
    {
      title: "Total Births (1971-2023)",
      value: "3,158,034",
      icon: Users,
      trend: "down",
      description: "Decreasing by 461 births per year"
    },
    {
      title: "Average Annual Births",
      value: "60,731",
      icon: Calendar,
      trend: "neutral",
      description: "Over 52-year period"
    },
    {
      title: "Average Unemployment Rate",
      value: "6.7%",
      icon: Briefcase,
      trend: "down",
      description: "Decreasing by 0.04% per year"
    },
    {
      title: "Peak Birth Year",
      value: "1971",
      icon: TrendingUp,
      trend: "up",
      description: "86,728 births recorded"
    }
  ]

  const keyFindings = [
    {
      title: "Declining Birth Rates",
      description: "Scotland has experienced a consistent decline in birth rates from 1971 to 2023, with the lowest recorded births in 2023 (45,935).",
      impact: "High"
    },
    {
      title: "Unemployment Trends",
      description: "Unemployment rates have generally decreased over the period, with peaks during economic recessions and lows during periods of growth.",
      impact: "Medium"
    },
    {
      title: "Demographic Transition",
      description: "The data suggests Scotland is undergoing a demographic transition typical of developed nations, with declining fertility rates.",
      impact: "High"
    }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-slate-50">
      {/* Header */}
      <motion.header 
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : -50 }}
        transition={{ duration: 0.8 }}
        className="bg-white/80 backdrop-blur-sm border-b border-slate-200 sticky top-0 z-50"
      >
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
                <BarChart3 className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-slate-900">Scotland Analysis</h1>
                <p className="text-sm text-slate-600">Economic & Demographic Insights</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <MapPin className="w-4 h-4 text-slate-500" />
              <span className="text-sm text-slate-600">Scotland, UK</span>
            </div>
          </div>
        </div>
      </motion.header>

      {/* Hero Section */}
      <motion.section 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 30 }}
        transition={{ duration: 0.8, delay: 0.2 }}
        className="container mx-auto px-6 py-12"
      >
        <div className="text-center max-w-4xl mx-auto">
          <Badge variant="secondary" className="mb-4">
            Data Analysis • 1971-2023
          </Badge>
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6">
            Economic & Demographic Analysis
            <span className="block text-blue-600">of Scotland</span>
          </h2>
          <p className="text-xl text-slate-600 mb-8 leading-relaxed">
            Comprehensive analysis of birth rates, unemployment trends, and demographic patterns 
            spanning over five decades of Scottish data.
          </p>
        </div>
      </motion.section>

      {/* Statistics Grid */}
      <motion.section 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 30 }}
        transition={{ duration: 0.8, delay: 0.4 }}
        className="container mx-auto px-6 py-8"
      >
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {stats.map((stat, index) => (
            <motion.div
              key={stat.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 20 }}
              transition={{ duration: 0.6, delay: 0.6 + index * 0.1 }}
            >
              <Card className="hover:shadow-lg transition-all duration-300 border-0 bg-white/70 backdrop-blur-sm">
                <CardHeader className="pb-3">
                  <div className="flex items-center justify-between">
                    <stat.icon className="w-8 h-8 text-blue-600" />
                    {stat.trend === 'up' && <TrendingUp className="w-4 h-4 text-green-500" />}
                    {stat.trend === 'down' && <TrendingDown className="w-4 h-4 text-red-500" />}
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <p className="text-2xl font-bold text-slate-900">{stat.value}</p>
                    <p className="text-sm font-medium text-slate-700">{stat.title}</p>
                    <p className="text-xs text-slate-500">{stat.description}</p>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </motion.section>

      {/* Analysis Chart */}
      <motion.section 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 30 }}
        transition={{ duration: 0.8, delay: 0.8 }}
        className="container mx-auto px-6 py-12"
      >
        <Card className="border-0 bg-white/70 backdrop-blur-sm shadow-xl">
          <CardHeader className="text-center">
            <CardTitle className="text-2xl text-slate-900">Comprehensive Data Visualization</CardTitle>
            <CardDescription className="text-slate-600">
              Interactive charts showing trends in births, unemployment, and correlations over time
            </CardDescription>
          </CardHeader>
          <CardContent className="p-8">
            <div className="relative overflow-hidden rounded-lg bg-white shadow-inner">
              <img 
                src={analysisChart} 
                alt="Economic and Demographic Analysis Chart" 
                className="w-full h-auto"
              />
            </div>
          </CardContent>
        </Card>
      </motion.section>

      {/* Key Findings */}
      <motion.section 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 30 }}
        transition={{ duration: 0.8, delay: 1.0 }}
        className="container mx-auto px-6 py-12"
      >
        <div className="text-center mb-12">
          <h3 className="text-3xl font-bold text-slate-900 mb-4">Key Findings</h3>
          <p className="text-slate-600 max-w-2xl mx-auto">
            Critical insights derived from the comprehensive analysis of Scottish demographic and economic data
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {keyFindings.map((finding, index) => (
            <motion.div
              key={finding.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: isVisible ? 1 : 0, y: isVisible ? 0 : 20 }}
              transition={{ duration: 0.6, delay: 1.2 + index * 0.2 }}
            >
              <Card className="h-full border-0 bg-white/70 backdrop-blur-sm hover:shadow-lg transition-all duration-300">
                <CardHeader>
                  <div className="flex items-center justify-between mb-2">
                    <CardTitle className="text-lg text-slate-900">{finding.title}</CardTitle>
                    <Badge variant={finding.impact === 'High' ? 'destructive' : 'secondary'}>
                      {finding.impact} Impact
                    </Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-slate-600 leading-relaxed">{finding.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </motion.section>

      {/* Footer */}
      <motion.footer 
        initial={{ opacity: 0 }}
        animate={{ opacity: isVisible ? 1 : 0 }}
        transition={{ duration: 0.8, delay: 1.4 }}
        className="bg-slate-900 text-white py-12 mt-16"
      >
        <div className="container mx-auto px-6">
          <div className="text-center">
            <div className="flex items-center justify-center space-x-3 mb-4">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <BarChart3 className="w-5 h-5 text-white" />
              </div>
              <h4 className="text-xl font-bold">Scotland Analysis</h4>
            </div>
            <p className="text-slate-400 mb-6">
              Comprehensive economic and demographic analysis for informed decision-making
            </p>
            <div className="flex flex-wrap justify-center gap-4 text-sm text-slate-400">
              <span>Data Period: 1971-2023</span>
              <span>•</span>
              <span>Sources: National Records of Scotland, ONS</span>
              <span>•</span>
              <span>Analysis: Economic & Demographic Trends</span>
            </div>
          </div>
        </div>
      </motion.footer>
    </div>
  )
}

export default App

