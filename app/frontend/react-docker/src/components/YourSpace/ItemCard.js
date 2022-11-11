import React from 'react';
import Card from 'react-bootstrap/Card';
import './ItemCard.css'

export function ItemCard() {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="https://eldenring.fanapis.com/images/items/17f69e47912l0i1z0lip3kamll88h.png" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

