import { Component, OnInit } from '@angular/core';
import { StockService } from 'src/app/services/stock.service';
import { MatDialog } from '@angular/material/dialog';
import { StockOrderModalComponent } from '../stock-order-modal/stock-order-modal.component';

@Component({
  selector: 'app-stock-listing',
  templateUrl: './stock-listing.component.html',
  styleUrls: ['./stock-listing.component.css'],
})
export class StockListingComponent implements OnInit {
  stocks: any[] = [];
  filteredStocks: any[] = [];
  searchQuery: string = '';

  constructor(private stockService: StockService, private dialog: MatDialog) {}

  ngOnInit(): void {
    this.fetchStocks();
  }

  fetchStocks(): void {
    this.stockService.getStocks().subscribe(
      (data) => {
        this.stocks = data;
        this.filteredStocks = data; // Initialize filtered stocks
        console.log(this.stocks)
      },
      (error) => {
        console.error('Error fetching stocks:', error);
      }
    );
  }

  searchStocks(): void {
    this.filteredStocks = this.stocks.filter((stock) =>
      stock.ticker_symbol.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }

  openOrderModal(stock: any): void {
    const dialogRef = this.dialog.open(StockOrderModalComponent, {
      width: '400px',
      data: { stock },
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        console.log('Order placed successfully:', result);
      }
    });
  }
}
