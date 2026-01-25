head = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>NASA – Today's Headlines</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #f8f9fa;
      color: #1a1a1a;
      line-height: 1.5;
    }

    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 16px;
    }

    /* Banner / Ad space */
    .banner {
      background: linear-gradient(135deg, #2c3e50 0%, #1a2634 100%);
      color: white;
      text-align: center;
      padding: 90px 20px 70px;
      margin-bottom: 32px;
      position: relative;
      overflow: hidden;
    }

    .banner::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 30% 70%, rgba(255,255,255,0.08) 0%, transparent 60%);
      pointer-events: none;
    }

    .banner h1 {
      font-size: 2.1rem;
      font-weight: 600;
      margin-bottom: 8px;
    }

    .banner p {
      font-size: 1.1rem;
      opacity: 0.9;
      max-width: 600px;
      margin: 0 auto;
    }

    /* Main grid - three columns */
    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 32px;
      padding: 20px 0 60px;
    }

    .column {
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      overflow: hidden;
    }

    .column-header {
      background: #0d47a1;
      color: white;
      padding: 16px 20px;
      font-size: 1.25rem;
      font-weight: 600;
      border-bottom: 1px solid #0b3d8c;
    }

    .story-list {
      padding: 12px 0;
    }

    .story {
      padding: 16px 20px;
      border-bottom: 1px solid #eee;
      transition: background-color 0.12s;
    }

    .story:hover {
      background-color: #f8fbff;
    }

    .story:last-child {
      border-bottom: none;
    }

    .story a {
      color: #0d47a1;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 500;
      display: block;
    }

    .story a:hover {
      color: #003087;
      text-decoration: underline;
    }

    .story-time {
      font-size: 0.82rem;
      color: #666;
      margin-top: 6px;
    }

    @media (max-width: 900px) {
      .news-grid {
        grid-template-columns: 1fr;
        gap: 24px;
      }
      
      .banner {
        padding: 70px 16px 50px;
      }
      
      .banner h1 {
        font-size: 1.8rem;
      }
    }
  </style>
</head>
<body>

<div class="container">

  <!-- Banner / Advertisement space -->
  <header class="banner">
    <h1>NASA Report</h1>
    <p>Quality headlines from trusted sources • Updated live</p>
    <!-- You can replace this whole block with real ad code -->
    <!-- <div style="height:90px; background:#e0e0e0; margin:30px auto; max-width:728px; border-radius:8px;">
      [ Advertisement / Leaderboard 728×90 ]
    </div> -->
  </header>

  <!-- Three-column news layout -->
  <main class="news-grid">
"""
footer = """
  </main>

</div>

</body>
</html>
"""
