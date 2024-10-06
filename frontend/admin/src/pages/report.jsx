import React, { useState, useEffect } from 'react';
import { Page, Navbar, Block, Progressbar } from 'framework7-react';
import { Pie } from 'react-chartjs-2';
import Chart from 'chart.js/auto';

const BaseURL = 'http://0.0.0.0';

const pieChartColors = [
  '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
  '#FF9F40', '#66FF66', '#FF3333', '#99CCFF', '#FFCCCC',
  '#CCCCFF', '#339966', '#FF6666', '#FFCC99', '#99CC33',
  '#6666CC', '#D97041', '#C7604C', '#21323D', '#9D9B7F'
];

const ReportPage = () => {
  const [loading, setLoading] = useState(true);
  const [insightsData, setInsightsData] = useState([]);
  const [psychologicalInsights, setPsychologicalInsights] = useState([]);
  const [professionalPotentials, setProfessionalPotentials] = useState([]);
  const [risks, setRisks] = useState([
    { name: "Cyberbullying", level: 0 },
    { name: "Exposure to Sensitive Content", level: 0 },
    { name: "Online Predators", level: 0 },
    { name: "Privacy Breaches", level: 0 },
    { name: "Excessive Screen Time", level: 0 },
    { name: "Social Media Addiction", level: 0 },
    { name: "Misinformation Exposure", level: 0 },
    { name: "In-App Purchases", level: 0 },
    { name: "Malware/Virus Exposure", level: 0 },
    { name: "gambling_betting_content", level: 0 },
  ]);

  useEffect(() => {
    Promise.all([
      fetch(`${BaseURL}/insights`).then(res => res.json()),
      fetch(`${BaseURL}/psychological-insights`).then(res => res.json()),
      fetch(`${BaseURL}/professional-potentials`).then(res => res.json()),
      fetch(`${BaseURL}/risks`).then(res => res.json())
    ]).then(([insightsRes, psychRes, profRes, risksRes]) => {
      const pieData = insightsRes.insights.map(insight => ({
        label: insight.interest_name,
        value: parseFloat(insight.percent.replace('%', ''))
      }));

      setInsightsData({
        labels: pieData.map(d => d.label),
        datasets: [{
          data: pieData.map(d => d.value),
          backgroundColor: pieData.map((_, index) => pieChartColors[index % pieChartColors.length]),
          borderColor: pieChartColors,
          borderWidth: 1,
        }]
      });

      setPsychologicalInsights(psychRes.psychological_insights);
      setProfessionalPotentials(profRes.professional_potentials);

      const newRisks = risks.map(risk => ({
        ...risk,
        level: risksRes.risks.some(r => r.risk_type === risk.name) ? 1 : 0
      }));
      setRisks(newRisks);

      setLoading(false);
    }).catch(error => {
      console.error('Failed to fetch data:', error);
      setLoading(false);
    });
  }, []);

  return (
    <Page>
      <Navbar title="Dashboard Report" backLink="Back" />
      {loading ? (
        <Progressbar infinite color="multi" />
      ) : (
        <div className="p-4" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '20px' }}>
          <Block strong>
            <h2>Interests Pie Chart</h2>
            <Pie data={insightsData} />
          </Block>

          <Block strong>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div>
                <h2>Psychological Insights</h2>
                <ul>
                  {psychologicalInsights.map((insight, index) => (
                    <li key={index}>{insight.insight}</li>
                  ))}
                </ul>
              </div>
              <div>
                <h2>Professional Potentials</h2>
                <ul>
                  {professionalPotentials.map((potential, index) => (
                    <li key={index}>{potential.potential}</li>
                  ))}
                </ul>
              </div>
            </div>
          </Block>

          <Block strong>
            <h2>Risk Assessment</h2>
            <ul>
              {risks.map((risk, index) => (
                <li key={index} style={{ color: risk.level > 0 ? 'red' : 'green' }}>
                  {risk.name}: {risk.level > 0 ? 'Detected' : 'Safe'}
                </li>
              ))}
            </ul>
          </Block>
        </div>
      )}
    </Page>
  );
};

export default ReportPage;
