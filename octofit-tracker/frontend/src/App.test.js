import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Octofit Tracker heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/Welcome to Octofit Tracker!/i);
  expect(headingElement).toBeInTheDocument();
});
