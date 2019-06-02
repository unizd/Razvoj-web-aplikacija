import { Component, OnInit } from '@angular/core';
import { AboutModel } from '../models/about-model';
import { ServiceService } from '../service.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

	about: AboutModel;

	constructor(private serviceService: ServiceService) {
		
	}

	ngOnInit() {
		this.getAbout();
	}
	
	getAbout() {
		this.serviceService.getAbout().subscribe(data => {
				this.about = data;
		})
    }

}
