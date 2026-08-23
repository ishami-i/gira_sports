import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import SiteLayout from './layouts/siteLayout'
import HomePage from './content/HomePage'
import PlaceholderPage from './content/PlaceholderPage'
import ArticlePage from './content/ArticlePage'
import EditorialWritingLayout from './content/WritingArticlePage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Full-bleed composer, no header/footer chrome */}
        <Route path="/write" element={<EditorialWritingLayout />} />

        <Route element={<SiteLayout />}>
          <Route index element={<Navigate to="/home" replace />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/scores" element={<PlaceholderPage title="Scores & Fixtures" description="Live scores and upcoming fixtures land here soon." />} />
          <Route path="/watch" element={<PlaceholderPage title="Watch" description="Highlights and live streams are on the way." />} />
          <Route path="/blog" element={<PlaceholderPage title="Blog" description="Browse every match report and analysis piece." />} />
          <Route path="/blog/demo" element={<ArticlePage />} />
          <Route path="/forums" element={<PlaceholderPage title="Forums" description="Join the conversation with other fans." />} />
          <Route path="/privacy" element={<PlaceholderPage title="Privacy Policy" />} />
          <Route path="/terms" element={<PlaceholderPage title="Terms of Service" />} />
          <Route path="/contact" element={<PlaceholderPage title="Contact Us" />} />
          <Route path="*" element={<PlaceholderPage title="Page not found" description="That page doesn't exist yet." />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
