import React from 'react';
import Card from 'react-bootstrap/Card';
import './ItemCard.css'

export function ItemCard({ItemName, ItemImg, ItemText}) {
  return (
    <Card style={{ width: '500px'}} className='card'>
      <Card.Img variant="top" src={ItemImg} />
      <Card.Body>
        <Card.Title>{ItemName}</Card.Title>
        <Card.Text>
          {ItemText}
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

