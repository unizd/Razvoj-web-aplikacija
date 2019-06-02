import { Component, OnInit } from '@angular/core';
import { PortfolioModel } from '../models/portfolio-model';
import { ServiceService } from '../service.service';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.css']
})
export class PortfolioComponent implements OnInit {

	portfolio: PortfolioModel[];

	constructor(private serviceService: ServiceService) {
		
	}

	ngOnInit() {
		this.getPortfolio();
	}
	
	getPortfolio() {
		this.serviceService.getPortfolio().subscribe(data => {
				this.portfolio = data;
		})
    }

}
