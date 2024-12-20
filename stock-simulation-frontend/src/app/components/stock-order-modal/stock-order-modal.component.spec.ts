import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StockOrderModalComponent } from './stock-order-modal.component';

describe('StockOrderModalComponent', () => {
  let component: StockOrderModalComponent;
  let fixture: ComponentFixture<StockOrderModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StockOrderModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StockOrderModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
