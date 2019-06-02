import { Component, OnInit } from '@angular/core';
import { ContactModel } from '../models/contact-model';
import { ServiceService } from '../service.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

	contact: ContactModel;

	constructor(private serviceService: ServiceService) {
		
	}

	ngOnInit() {
		this.getContact();
	}
	
	getContact() {
		this.serviceService.getContact().subscribe(data => {
				this.contact = data;
		})
    }

}
